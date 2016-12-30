#!/bin/bash
echo 'lego-nxt-sound' > /sys/class/lego-port/port1/set_device
python3 `which rpyc_classic.py`
