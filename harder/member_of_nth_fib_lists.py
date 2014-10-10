from nth_fib_lists import nth_fib_lists


def member_of_nth_fib_lists(listA, listB, needle):
    my_list = nth_fib_lists(listA, listB, len(needle))
    flag = True
    for i in range(0, len(needle)):
        if my_list[i] == needle[0]:
            flag = True
            ix = i
            for v in needle:
                if v != my_list[ix]:
                    flag = False
                    break
                ix += 1
            if flag is True:
                return True
    return (flag)


print (member_of_nth_fib_lists([7, 11], [2], [11, 7, 2, 2, 7]))
