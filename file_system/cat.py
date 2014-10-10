import sys



def main():
    for arg in sys.argv:
        if arg != "cat.py":
            filename = arg
            file = open(filename, "r")
            content = file.read()
            print (content)

if __name__ == '__main__':
    main()
