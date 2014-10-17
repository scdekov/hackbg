def groupby(func, seq):
    dic = {}
    for se in seq:
        key = func(se)
        if key in dic:
            dic[key].append(se)
        else:
            dic[key] = [se]
    return dic

