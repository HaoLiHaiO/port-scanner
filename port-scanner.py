#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("Please enter an IP address: ")
port = str(input("Please enter a port: "))

def portScanner(port):
    if s.connect_ex((host, int(port))):
        print("The port is closed.")
    else:
        print("The port is open.")

portScanner(port)