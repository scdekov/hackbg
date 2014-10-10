import sys


def main():
    content = ""
    for arg in sys.argv:
        if arg != "concat_files.py":
            file = open(arg, "r")
            content += file.read()
            file.close()
    file = open("MEGATRON", "w")
    file.write(content)
    file.close()




if __name__ == '__main__':
    main()
