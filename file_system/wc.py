import sys


def wc():
    file = open(sys.argv[2], "r")
    content = file.read()
    if sys.argv[1] == "chars":
        return (len(content))
    elif sys.argv[1] == "words":
        content = content.split(" ")
        return (len(content))
    elif sys.argv[1] == "lines":
        file.close()
        return (len(open(sys.argv[2]).readlines()) + 1)
