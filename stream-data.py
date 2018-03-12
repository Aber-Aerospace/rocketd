import time
from sense_hat import SenseHat

s = SenseHat()


def main():
    while True:
        o = s.get_orientation()
        print("pitch: {:3.2f}, roll: {:3.2f}, y: {:3.2f}".format(o['pitch'], o['roll'], a['yaw']))
        a = s.get_accelerometer_raw
        print("x: {:3.2f}, y: {:3.2f}, z: {:3.2f}".format(a['x'], a['y'], a['z']))

if __name__ == '__main__':
    main()
