import sys

def main():
    sum = 0
    file = open(sys.argv[1], "r")
    content = file.read()
    content = content.split()
    for el in content:
        sum += int(el)
    print (sum)
    file.close()


if __name__ == '__main__':
    main()
