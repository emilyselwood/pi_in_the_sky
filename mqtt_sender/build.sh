# !/bin/bash

EDC_ROOT=/home/pi/edc-c-client
OUTPUT=mqtt-sender

g++ -Wall \
 -I$EDC_ROOT/edcclient/ -I$EDC_ROOT/protobuf/src/ -I$EDC_ROOT/org.eclipse.paho.mqtt.c/src/ -I$EDC_ROOT/config \
 -L$EDC_ROOT/protobuf/src/.libs/ -L$EDC_ROOT/org.eclipse.paho.mqtt.c/build/output/ \
 -o $OUTPUT \
 i2c-host.c mqtt-sender.c $EDC_ROOT/edcclient/edcpayload.pb.cc $EDC_ROOT/edcclient/config.cpp \
 -lpaho-mqtt3c -lpthread -lprotobuf