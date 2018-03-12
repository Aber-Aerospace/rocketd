import time
from sense_hat import SenseHat

s = SenseHat()


def main():
    while True:
        o = sense.get_orientation()
        print("pitch: {3:.2f}, roll: {3:.2f}, y: {3:.2f}".format(o['pitch'], o['roll'], p['yaw']))



if __name__ == '__main__':
    main()
