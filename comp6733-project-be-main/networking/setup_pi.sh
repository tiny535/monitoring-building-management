#!/bin/bash

echo 'Installing tcpdump'
apt-get install tcpdump

echo 'tcpdump installed'
echo 'Setting wlan1 to monitor mode'
ip link set wlan1 down
iw wlan1 set monitor none
ip link set wlan1 up
echo 'Check if wlan1 is set to monitor mode'
iw dev
