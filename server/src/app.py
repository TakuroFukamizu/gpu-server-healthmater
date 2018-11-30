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

def task(ser):
    records = []
    try:
        for record in get_smi_record():
            records.append(record)
    except Exception as ex:
        print(ex)
        print(traceback.format_exc())
        return
    gpu_value = records[0].gpu_utilization

    # with serial.Serial(SERIAL_PORT, 9600, timeout=1) as ser:
    #     value = int(gpu_value)
    #     value = value.to_bytes(1, 'little')
    #     ser.write(value)
    # ser.close()
    value = int(gpu_value)
    value = value.to_bytes(1, 'little')
    ser.write(value)
    print(time.time(), gpu_value, ser.name, value)


if __name__ == "__main__":
    with serial.Serial(SERIAL_PORT, 9600, timeout=1) as ser:
        while True:
            task(ser)
            time.sleep(1)
    ser.close()


