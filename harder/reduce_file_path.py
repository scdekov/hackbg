def reduce_file_path(path):
    path = path.split("/")
    for i, v in enumerate(path):
        if v == '..':
            del path[i]
        if v == '':
            del path[i]
    return "/".join(path)



print (reduce_file_path("/etc/../etc/../etc/../"))
