import logging
import sys
from flask import Flask

from audioCommandLib import zr6Lib, monoLib, denonLib

sys.path.append('/home/admin/.local/usr/bin')

app = Flask(__name__)
logging.basicConfig(filename='/tmp/homeAudioRest.log', level=logging.INFO)


def content_return_mono(ret):
    if ret.find("#"):
        return "{}", 200, {'Content-Type': 'text/json; charset=utf-8'}
    else:
        return ret, 500, {'Content-Type': 'text/json; charset=utf-8'}


def content_return_denon(ret):
    if ret == 200:
        return "{}", 200, {'Content-Type': 'text/json; charset=utf-8'}
    else:
        return str(ret), 500, {'Content-Type': 'text/json; charset=utf-8'}


def content_return_zr6(ret):
    if ret.find("OK"):
        return "{}", 200, {'Content-Type': 'text/json; charset=utf-8'}
    else:
        return ret, 500, {'Content-Type': 'text/json; charset=utf-8'}


@app.route("/backyard/zones/on", methods=['GET'])
def backyard_zones_all_on():
    return content_return_mono(monoLib.set_all_zones_on())


@app.route("/backyard/zones/off", methods=['GET'])
def backyard_zones_all_off():
    return content_return_mono(monoLib.set_all_zones_off())


# @app.route("/backyard/zones/<zone>/<command>", methods=['GET'])
# def house_zones_command(zone, command):


@app.route("/house/zones/on", methods=['GET'])
def house_zones_all_on():
    return content_return_zr6(zr6Lib.set_all_zones_on())


@app.route("/house/zones/off", methods=['GET'])
def house_zones_all_off():
    return content_return_zr6(zr6Lib.set_all_zones_off())


@app.route("/house/zones/<zone>/<command>", methods=['GET'])
def house_zones_command(zone, command):
    zone_in = map_zones(zone)
    if command == "on":
        return content_return_zr6(zr6Lib.set_zone_on(zone_in))
    if command == "off":
        return content_return_zr6(zr6Lib.set_zone_off(zone_in))

    command_in = map_command(command)
    return content_return_zr6(zr6Lib.send_zone_command(zone_in, command_in))


def map_command(command_in):
    if command_in == "up":
        return zr6Lib.COMMAND_VOLUME_UP
    if command_in == "down":
        return zr6Lib.COMMAND_VOLUME_DOWN


def map_zones(zone_in):
    if zone_in == "1":
        return zr6Lib.ZONE_01
    if zone_in == "2":
        return zr6Lib.ZONE_02
    if zone_in == "3":
        return zr6Lib.ZONE_03
    if zone_in == "4":
        return zr6Lib.ZONE_04
    if zone_in == "5":
        return zr6Lib.ZONE_05
    if zone_in == "6":
        return zr6Lib.ZONE_06
    if zone_in == "7":
        return zr6Lib.ZONE_07
    if zone_in == "8":
        return zr6Lib.ZONE_08
    if zone_in == "9":
        return zr6Lib.ZONE_09
    if zone_in == "10":
        return zr6Lib.ZONE_10
    if zone_in == "11":
        return zr6Lib.ZONE_11
    if zone_in == "12":
        return zr6Lib.ZONE_12


@app.route("/house/denon/off", methods=['GET'])
def denon_on():
    return content_return_denon(denonLib.power_off())


@app.route("/house/denon/roku", methods=['GET'])
def denon_roku():
    return content_return_denon(denonLib.select_roku())


@app.route("/house/denon/sonos", methods=['GET'])
def denon_sonos():
    return content_return_denon(denonLib.select_sonos())
