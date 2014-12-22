def get_file(file):
    return open(file).read


def split_lines(text):
    return text.split("\n")


def is_line_empty(line):
    return line.strip() == ""


def is_line_import(line):

