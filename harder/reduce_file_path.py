def reduce_file_path(path):
    if path == "/" or path == "":
        return "/"
    path = path.split("/")
    print path
    for i, v in enumerate(path):
        if v == '..':
            del path[i]
            del path[i - 1]
        if v == '':
            del path[i]
    if "/".join(path) == "":
        return "/"
    return "/".join(path)

reduce_file_path("/srv/../")
