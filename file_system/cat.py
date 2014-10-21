import sys



def cat():
    filename = sys.argv[1]
    file = open(filename, "r")
    content = file.read()
    return (content)

