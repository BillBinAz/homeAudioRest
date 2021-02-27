#!/bin/bash
rm /tmp/zr6_flask.log
cd /home/admin/nilesZR6Rest
export FLASK_APP=get_handler.py
/usr/bin/python3 -m flask run --host='0.0.0.0' --port=8081 --no-reload
