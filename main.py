import os
import sys

from plugins.PyLogger import pylogger


os.chdir(os.path.dirname(os.path.realpath(__file__)))


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    pass


if __name__ == '__main__':
    main()
