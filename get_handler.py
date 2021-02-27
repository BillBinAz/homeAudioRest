import logging
import sys
from flask import Flask

from zr6CommandLib import zr6Lib

sys.path.append('/home/admin/.local/usr/bin')

app = Flask(__name__)
logging.basicConfig(filename='/tmp/zr6_flask.log', level=logging.INFO)


def content_return(ret):
    if ret:
        return {}, 200, {'Content-Type': 'text/json; charset=utf-8'}
    else:
        return {}, 500, {'Content-Type': 'text/json; charset=utf-8'}


@app.route("/zr6/zones/on", methods=['GET'])
def zones_all_on():
    return content_return(zr6Lib.set_whole_home_on())


@app.route("/zr6/zones/off", methods=['GET'])
def zones_all_off():
    return content_return(zr6Lib.set_whole_home_off())


@app.route("/zr6/zones/1/on", methods=['GET'])
def zone_1_on():
    return content_return(zr6Lib.set_zone_on(zr6Lib.ZONE_01))


@app.route("/zr6/zones/1/off", methods=['GET'])
def zone_1_off():
    return content_return(zr6Lib.set_zone_off(zr6Lib.ZONE_01))


@app.route("/zr6/zones/2/on", methods=['GET'])
def zone_2_on():
    return content_return(zr6Lib.set_zone_on(zr6Lib.ZONE_02))


@app.route("/zr6/zones/2/off", methods=['GET'])
def zone_2_off():
    return content_return(zr6Lib.set_zone_off(zr6Lib.ZONE_02))


@app.route("/zr6/zones/3/on", methods=['GET'])
def zone_3_on():
    return content_return(zr6Lib.set_zone_on(zr6Lib.ZONE_03))


@app.route("/zr6/zones/3/off", methods=['GET'])
def zone_3_off():
    return content_return(zr6Lib.set_zone_off(zr6Lib.ZONE_03))


@app.route("/zr6/zones/4/on", methods=['GET'])
def zone_4_on():
    return content_return(zr6Lib.set_zone_on(zr6Lib.ZONE_04))


@app.route("/zr6/zones/4/off", methods=['GET'])
def zone_4_off():
    return content_return(zr6Lib.set_zone_off(zr6Lib.ZONE_04))


@app.route("/zr6/zones/5/on", methods=['GET'])
def zone_5_on():
    return content_return(zr6Lib.set_zone_on(zr6Lib.ZONE_05))


@app.route("/zr6/zones/5/off", methods=['GET'])
def zone_5_off():
    return content_return(zr6Lib.set_zone_off(zr6Lib.ZONE_05))


@app.route("/zr6/zones/6/on", methods=['GET'])
def zone_6_on():
    return content_return(zr6Lib.set_zone_on(zr6Lib.ZONE_06))


@app.route("/zr6/zones/6/off", methods=['GET'])
def zone_6_off():
    return content_return(zr6Lib.set_zone_off(zr6Lib.ZONE_06))


@app.route("/zr6/zones/7/on", methods=['GET'])
def zone_7_on():
    return content_return(zr6Lib.set_zone_on(zr6Lib.ZONE_07))


@app.route("/zr6/zones/7/off", methods=['GET'])
def zone_7_off():
    return content_return(zr6Lib.set_zone_off(zr6Lib.ZONE_07))


@app.route("/zr6/zones/8/on", methods=['GET'])
def zone_8_on():
    return content_return(zr6Lib.set_zone_on(zr6Lib.ZONE_08))


@app.route("/zr6/zones/8/off", methods=['GET'])
def zone_8_off():
    return content_return(zr6Lib.set_zone_off(zr6Lib.ZONE_08))


@app.route("/zr6/zones/9/on", methods=['GET'])
def zone_9_on():
    return content_return(zr6Lib.set_zone_on(zr6Lib.ZONE_09))


@app.route("/zr6/zones/9/off", methods=['GET'])
def zone_9_off():
    return content_return(zr6Lib.set_zone_off(zr6Lib.ZONE_09))


@app.route("/zr6/zones/10/on", methods=['GET'])
def zone_10_on():
    return content_return(zr6Lib.set_zone_on(zr6Lib.ZONE_10))


@app.route("/zr6/zones/10/off", methods=['GET'])
def zone_10_off():
    return content_return(zr6Lib.set_zone_off(zr6Lib.ZONE_10))


@app.route("/zr6/zones/11/on", methods=['GET'])
def zone_11_on():
    return content_return(zr6Lib.set_zone_on(zr6Lib.ZONE_11))


@app.route("/zr6/zones/11/off", methods=['GET'])
def zone_11_off():
    return content_return(zr6Lib.set_zone_off(zr6Lib.ZONE_11))


@app.route("/zr6/zones/11/on", methods=['GET'])
def zone_11_on():
    return content_return(zr6Lib.set_zone_on(zr6Lib.ZONE_11))


@app.route("/zr6/zones/12/off", methods=['GET'])
def zone_12_off():
    return content_return(zr6Lib.set_zone_off(zr6Lib.ZONE_12))
