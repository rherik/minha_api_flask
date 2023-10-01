#!/bin/sh
CPU=`grep -c ^processor /proc/cpuinfo`
W=$(($CPU * 2))

flask db upgrade

exec gunicorn --bind 0.0.0.0:80 -w $W  'flaskApp:app'
