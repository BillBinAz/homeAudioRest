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


@app.route("/house/zones/on", methods=['GET'])
def house_zones_all_on():
    return content_return_zr6(zr6Lib.set_all_zones_on())


@app.route("/house/zones/off", methods=['GET'])
def house_zones_all_off():
    return content_return_zr6(zr6Lib.set_all_zones_off())


@app.route("/house/zones/1/on", methods=['GET'])
def zone_1_on():
    return content_return_zr6(zr6Lib.set_zone_on(zr6Lib.ZONE_01))


@app.route("/house/zones/1/off", methods=['GET'])
def zone_1_off():
    return content_return_zr6(zr6Lib.set_zone_off(zr6Lib.ZONE_01))


@app.route("/house/zones/2/on", methods=['GET'])
def zone_2_on():
    return content_return_zr6(zr6Lib.set_zone_on(zr6Lib.ZONE_02))


@app.route("/house/zones/2/off", methods=['GET'])
def zone_2_off():
    return content_return_zr6(zr6Lib.set_zone_off(zr6Lib.ZONE_02))


@app.route("/house/zones/3/on", methods=['GET'])
def zone_3_on():
    return content_return_zr6(zr6Lib.set_zone_on(zr6Lib.ZONE_03))


@app.route("/house/zones/3/off", methods=['GET'])
def zone_3_off():
    return content_return_zr6(zr6Lib.set_zone_off(zr6Lib.ZONE_03))


@app.route("/house/zones/4/on", methods=['GET'])
def zone_4_on():
    return content_return_zr6(zr6Lib.set_zone_on(zr6Lib.ZONE_04))


@app.route("/house/zones/4/off", methods=['GET'])
def zone_4_off():
    return content_return_zr6(zr6Lib.set_zone_off(zr6Lib.ZONE_04))


@app.route("/house/zones/5/on", methods=['GET'])
def zone_5_on():
    return content_return_zr6(zr6Lib.set_zone_on(zr6Lib.ZONE_05))


@app.route("/house/zones/5/off", methods=['GET'])
def zone_5_off():
    return content_return_zr6(zr6Lib.set_zone_off(zr6Lib.ZONE_05))


@app.route("/house/zones/6/on", methods=['GET'])
def zone_6_on():
    return content_return_zr6(zr6Lib.set_zone_on(zr6Lib.ZONE_06))


@app.route("/house/zones/6/off", methods=['GET'])
def zone_6_off():
    return content_return_zr6(zr6Lib.set_zone_off(zr6Lib.ZONE_06))


@app.route("/house/zones/7/on", methods=['GET'])
def zone_7_on():
    return content_return_zr6(zr6Lib.set_zone_on(zr6Lib.ZONE_07))


@app.route("/house/zones/7/off", methods=['GET'])
def zone_7_off():
    return content_return_zr6(zr6Lib.set_zone_off(zr6Lib.ZONE_07))


@app.route("/house/zones/8/on", methods=['GET'])
def zone_8_on():
    return content_return_zr6(zr6Lib.set_zone_on(zr6Lib.ZONE_08))


@app.route("/house/zones/8/off", methods=['GET'])
def zone_8_off():
    return content_return_zr6(zr6Lib.set_zone_off(zr6Lib.ZONE_08))


@app.route("/house/zones/9/on", methods=['GET'])
def zone_9_on():
    return content_return_zr6(zr6Lib.set_zone_on(zr6Lib.ZONE_09))


@app.route("/house/zones/9/off", methods=['GET'])
def zone_9_off():
    return content_return_zr6(zr6Lib.set_zone_off(zr6Lib.ZONE_09))


@app.route("/house/zones/10/on", methods=['GET'])
def zone_10_on():
    return content_return_zr6(zr6Lib.set_zone_on(zr6Lib.ZONE_10))


@app.route("/house/zones/10/off", methods=['GET'])
def zone_10_off():
    return content_return_zr6(zr6Lib.set_zone_off(zr6Lib.ZONE_10))


@app.route("/house/zones/11/on", methods=['GET'])
def zone_11_on():
    return content_return_zr6(zr6Lib.set_zone_on(zr6Lib.ZONE_11))


@app.route("/house/zones/11/off", methods=['GET'])
def zone_11_off():
    return content_return_zr6(zr6Lib.set_zone_off(zr6Lib.ZONE_11))


@app.route("/house/zones/12/on", methods=['GET'])
def zone_12_on():
    return content_return_zr6(zr6Lib.set_zone_on(zr6Lib.ZONE_12))


@app.route("/house/zones/12/off", methods=['GET'])
def zone_12_off():
    return content_return_zr6(zr6Lib.set_zone_off(zr6Lib.ZONE_12))


@app.route("/house/denon/off", methods=['GET'])
def denon_on():
    return content_return_mono(denonLib.power_off())


@app.route("/house/denon/roku", methods=['GET'])
def denon_roku():
    return content_return_mono(denonLib.select_roku())


@app.route("/house/denon/sonos", methods=['GET'])
def denon_sonos():
    return content_return_mono(denonLib.select_sonos())
