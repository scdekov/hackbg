def sort_fractions(fractions):
    dec = []
    for fr in fractions:
        dec.append(fr[0] / fr[1])
    for i in range(0, len(dec)):
        for j in range(len(dec) - 1 - i):
            if dec[j] > dec[j+1]:
                dec[j], dec[j+1] = dec[j+1], dec[j]
                fractions[j], fractions[j+1] = fractions[j+1], fractions[j]
    return fractions

print (sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))
