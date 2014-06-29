# !/bin/bash

EDC_ROOT=/home/pi/edc-c-client
OUTPUT=mqtt-sender

export LD_LIBRARY_PATH=$EDC_ROOT/org.eclipse.paho.mqtt.c/build/output/:$EDC_ROOT/protobuf/src/.libs/:${LD_LIBRARY_PATH}

./mqtt-sender $@