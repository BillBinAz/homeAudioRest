#!/usr/bin/env python3

import socket

import zr6

BUFFER_SIZE = 1024


def send_command(command):
    # Create a TCP/IP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((zr6.ZR6_IP, zr6.ZR6_PORT))

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
    return ""


def set_current_zone(zone_in):
    response = send_command(zr6.ZONE_SET_ACTIVE.format(zone=zone_in))
    if response == zr6.REQUEST_RESPONSE_SET_ACTIVE.format(zone=zone_in):
        return True
    else:
        return False


def get_current_zone():
    return send_command(zr6.REQUEST_STATUS)


def send_zone_command(zone_in, command_in):
    message = zr6.ZONE_SPECIFIC_COMMAND.format(zone=zone_in, command=command_in)
    response = send_command(message)

    if response == zr6.ZONE_SPECIFIC_COMMAND_RETURN.format(zone=zone_in, command=command_in):
        return True
    else:
        return False


def set_zone_on(zone_in):
    return send_zone_command(zone_in, zr6.COMMAND_SOURCE_SELECT_2)


def set_zone_off(zone_in):
    return send_zone_command(zone_in, zr6.COMMAND_OFF)


def set_whole_home_on():
    message = zr6.REQUEST_GLOBAL_COMMAND.format(command=zr6.COMMAND_SOURCE_SELECT_2)
    response = send_command(message)

    if response == zr6.REQUEST_GLOBAL_COMMAND.format(command=zr6.COMMAND_SOURCE_SELECT_2):
        return True
    else:
        return False


def set_whole_home_off():
    message = zr6.REQUEST_GLOBAL_COMMAND.format(command=zr6.COMMAND_OFF)
    response = send_command(message)

    if response == zr6.REQUEST_GLOBAL_COMMAND.format(command=zr6.COMMAND_OFF):
        return True
    else:
        return False


def main():
    set_current_zone(zr6.ZONE_05)
    print(get_current_zone())
    # set_zone_on(zr6.ZONE_05)
    # print(get_current_zone())
    # set_zone_off(zr6.ZONE_05)
    # print(get_current_zone())
    # set_whole_home_on()
    # set_whole_home_off()


main()
