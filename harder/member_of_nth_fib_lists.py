from nth_fib_lists import nth_fib_lists


def member_of_nth_fib_lists(listA, listB, needle):
    my_list = nth_fib_lists(listA, listB, len(needle) + 5)
    flag = False
    for i in range(0, len(my_list)):
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

