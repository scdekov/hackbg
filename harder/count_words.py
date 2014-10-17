def count_words(arr):
    dic = {}
    for word in arr:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    return dic

