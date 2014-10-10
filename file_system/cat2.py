import sys

def main():
    for arg in sys.argv:
        if arg != "cat2.py":
            file = open(arg, "r")
            content = file.read()
            print (content)
            file.close()







if __name__ == '__main__':
    main()
