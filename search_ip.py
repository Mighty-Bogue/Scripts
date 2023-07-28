# Script to search for any IPs occurence in every files in a directory
import os
import re

def find_ips_in_file(file_path):
    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    ips_found = set()

    with open(file_path, "r") as file:
        for line in file:
            ips = re.findall(ip_pattern, line)
            ips_found.update(ips)

    return ips_found

def main():
    directory_path = input("Enter the full path to the directory to search for IP addresses in files: ")
    ip_addresses = set()

    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            ips_in_file = find_ips_in_file(file_path)
            ip_addresses.update(ips_in_file)

    print("IP addresses found:")
    for ip in ip_addresses:
        print(ip)

if __name__ == "__main__":
    main()
