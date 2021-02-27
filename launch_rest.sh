#!/bin/bash
rm /tmp/homeAudioRest.log
cd /home/admin/homeAudioRest
export FLASK_APP=get_handler.py
/usr/bin/python3 -m flask run --host='0.0.0.0' --port=8081 --no-reload
