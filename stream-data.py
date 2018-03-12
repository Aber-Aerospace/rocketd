import time
from sense_hat import SenceHat

s = SenceHat()


def main():
    while True:
        orientation = sense.get_orientation()
        print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))



if __name__ == '__main__':
    main()
