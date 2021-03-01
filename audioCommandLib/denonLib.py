#!/usr/bin/env python3

import requests


DENON_IP = "192.168.2.80"
HTTP_COMMAND = "http://{host}/MainZone/index.put.asp"
COMMAND_POWER_ON = "PutZone_OnOff/ON"
COMMAND_POWER_OFF = "PutZone_OnOff/OFF"
COMMAND_SELECT_INPUT_CD = "PutZone_InputFunction/CD"
COMMAND_SELECT_INPUT_SAT_CBL = "PutZone_InputFunction/SAT/CBL"
COMMAND_ONE = "apsMainZone_WebUpdateStatus"
COMMAND_DATA = "{{ 'cmd0' : '{command}',  'cmd1' : 'apsMainZone_WebUpdateStatus'}}"


def send_command(host_in, command_in):
    #
    # use the Denon HTTP Layer
    url = HTTP_COMMAND.format(host=host_in)

    try:
        #
        # Post the data
        post_data = { 'cmd0': command_in,
                      'cmd1': 'apsMainZone_WebUpdateStatus'}
        ret = requests.post(url, verify=False, data=post_data)
        print(ret.text)
        ret.close()
        if ret.status_code != 200:
            print("Bad response from Denon. " + str(ret.status_code))
        return ret
    except Exception as e:
        return str(e)


def power_on():
    return send_command(DENON_IP, COMMAND_POWER_ON)


def power_off():
    return send_command(DENON_IP, COMMAND_POWER_OFF)


def select_sonos():
    ret = send_command(DENON_IP, COMMAND_POWER_ON)
    return ret + send_command(DENON_IP, COMMAND_SELECT_INPUT_CD)


def select_roku():
    ret = send_command(DENON_IP, COMMAND_POWER_ON)
    return ret + send_command(DENON_IP, COMMAND_SELECT_INPUT_SAT_CBL)


def debug():

    # standby
    # print(power_off())

    # Power on
    # print(power_on())

    # select CD
    # print(select_sonos())

    # select CBL
    print(select_roku())


def main():
    debug()


main()
