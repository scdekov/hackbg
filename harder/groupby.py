def groupby(func, seq):
    dic = {}
    counter = 0
    for se in seq:
        key = func(se)
        if key in dic:
            dic[key].append(se)
        else:
            dic[key] = [se]
    return dic

print (groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7]))

