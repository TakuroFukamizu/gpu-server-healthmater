#!/usr/bin/python
# -*- coding: utf-8 -*-

import traceback
import argparse
from envparse import env
from libs.watcher import get_smi_record
import time
import serial

# -----------

env.read_envfile()
SERIAL_PORT = env.str("SERIAL_PORT", default=8080)

# -----------

def task():
    records = []
    try:
        for record in get_smi_record():
            records.append(record)
    except Exception as ex:
        print(ex)
        print(traceback.format_exc())
        return
    gpu_value = records[0].gpu_utilization
    print(time.time(), gpu_value)

    with serial.Serial(SERIAL_PORT, 9600, timeout=1) as ser:
        value = int(gpu_value)
        value = value.to_bytes(1, 'little')
        ser.write(value)
    ser.close()


if __name__ == "__main__":
    while True:
        task()
        time.sleep(1)


