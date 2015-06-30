#!/bin/bash
SCRIPT_NAME=/home/pi/gpio/goal_reader.py
PID_FILE=/var/run/goal_reader.pid
export PYTHON_PATH=${PYTHON_PATH}:/home/pi/gpio/

case "$1" in
    start)
    echo "Starting goal reader script..."
    sudo python $SCRIPT_NAME &
    echo "$!" > $PID_FILE
    ;;
    stop)
    echo "Stopping goal reader script..."
    kill `cat $PID_FILE`
    ;;
    *)
    echo "Usage $0 {start|stop}"
    ;;
esac
