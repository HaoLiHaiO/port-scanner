#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# hackthissite.org's IP
host = "137.74.187.103"
port = 443

def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed.")
    else:
        print("The port is open.")

portScanner(port)