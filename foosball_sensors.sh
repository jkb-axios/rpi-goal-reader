#!/bin/bash
SCRIPT_NAME=/home/pi/gpio/foosball_sensors.py
PID_FILE=/var/run/foosball_sensors.pid
export PYTHON_PATH=${PYTHON_PATH}:/home/pi/gpio/

case "$1" in
    start)
    echo "Starting goals script..."
    sudo python $SCRIPT_NAME &
    echo "$!" > $PID_FILE
    ;;
    stop)
    echo "Stopping goals script..."
    kill `cat $PID_FILE`
    ;;
    *)
    echo "Usage $0 {start|stop}"
    ;;
esac
