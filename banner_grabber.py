#!/usr/bin/env python3

import socket # We need it to create a TCP connection

def main():
    IP = input("Target IP: ")
    PORT = input("Target Port: ")
    PORT = int(PORT)
    print(banner_grab(IP, PORT))

def banner_grab(IP, PORT):
    try: 
        s = socket.socket() # A variable from the socket class
        s.settimeout(5) # We set a timeout
        s.connect((IP, PORT)) # connection to a particular IP and port
        result = s.recv(1024).decode("utf-8") # Read the datas et store them in the variable "result". The decode part allows us to get rid of the "b'" and "\r\n'" in the answer  
        s.close() # Close the connection
        return result
    except:
        return "No banner to grab or the port may be closed. You should also check if this is the right IP !"

if __name__ == '__main__': 
    main()  
