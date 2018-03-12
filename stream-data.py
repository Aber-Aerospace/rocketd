import time
import math
from sense_hat import SenseHat

s = SenseHat()


def main():
    while True:
        o = s.get_orientation()

        if(5 > 0['pitch'] or o['pitch'] > 355):
            print("CHUTE")
        else:
            print("")

        print("pitch: {:3.2f}, roll: {:3.2f}, y: {:3.2f}".format(o['pitch'], o['roll'], a['yaw']))

if __name__ == '__main__':
    main()
