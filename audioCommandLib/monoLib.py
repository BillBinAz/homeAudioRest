#!/usr/bin/env python3

import socket

BUFFER_SIZE = 1024
GLOBAL_CACHE_IP = "192.168.2.152"
SERIAL_PORT = 4999

REQUEST_ALL_ZONES_ON = "<10PR01\r"
REQUEST_ALL_ZONES_OFF = "<10PR00\r"
FAILED = "UNKNOWN FAILURE"


def send_command(command):
    # Create a TCP/IP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((GLOBAL_CACHE_IP, SERIAL_PORT))

        # Send data
        s.send(command.encode())

        # receive data
        data = s.recv(BUFFER_SIZE).decode()
        s.close()
        return data
    except Exception as e:
        print(e)
    finally:
        s.close()
    return FAILED


def set_all_zones_on():
    return send_command(REQUEST_ALL_ZONES_ON)


def set_all_zones_off():
    return send_command(REQUEST_ALL_ZONES_OFF)


def debug():
    print(set_all_zones_on())
    print(set_all_zones_off())

# def main():
#    debug()


# main()
