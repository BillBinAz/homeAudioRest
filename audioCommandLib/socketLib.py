#!/usr/bin/env python3

import socket

BUFFER_SIZE = 1024
FAILED = "UNKNOWN FAILURE"


def send_command(command, ip, port):
    # Create a TCP/IP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((ip, port))

        # Send data
        s.send(command.encode())

        # receive data
        data = s.recv(BUFFER_SIZE).decode()
        s.close()
        return data
    except Exception as e:
        return str(e)
    finally:
        s.close()
    return FAILED
