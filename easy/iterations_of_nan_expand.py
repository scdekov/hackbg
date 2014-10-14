def iterations_of_nan_expand(expanded):
    if expanded == "":
        return 0
    expanded = expanded.split(" ")
    if expanded.count("Not") == expanded.count("a") and expanded.count("NaN") == 1:
        if len(expanded) == expanded.count("Not") * 2 + 1:
            return expanded.count("Not")
    return False


def main():
    print (iterations_of_nan_expand("Show these people!"))


if __name__ == '__main__':
    main()
