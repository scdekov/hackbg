import sys


def main():
    file = open(sys.argv[2], "r")
    content = file.read()
    if sys.argv[1] == "chars":
        print (len(content))
    elif sys.argv[1] == "words":
        content = content.split(" ")
        print (len(content))
    elif sys.argv[1] == "lines":
        file.close()
        print (len(open(sys.argv[2]).readlines()) + 1)

if __name__ == '__main__':
    main()
