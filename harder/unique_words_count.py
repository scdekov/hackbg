def unique_words_count(arr):
    ar = []
    for word in arr:
        if ar.count(word) == 0:
            ar.append(word)
    return len(ar)

print (unique_words_count(["python", "python", "python", "ruby"]))