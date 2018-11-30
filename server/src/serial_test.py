#coding:utf-8

import serial

port = '/dev/tty.usbmodem143201'

start_flag = 255
start_flag = start_flag.to_bytes(1, 'little')
print(start_flag)

def main():
    with serial.Serial(port, 9600, timeout=1) as ser:
        print(ser.name)

        while True:
            # flag = bytes(input(), 'utf-8')
            value = int(input())

            if 100 < value:
                break

            value = value.to_bytes(1, 'little')
            # ser.write(start_flag)
            ser.write(value)
            line = ser.readline()
            print(line)
        ser.close()

if __name__ == "__main__":
    main()