import sys
from random import randint


def main():
    file = open(sys.argv[1], "w")
    for i in range(1, int(sys.argv[2])):
        file.write(str(randint(1, 1000))+" ")
    file.close()
if __name__ == '__main__':
    main()
