def what_is_my_sign(day, month):
    signs = ["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"]
    biggest_day_for_sign = {4: 20, 5: 21, 6: 21, 7: 22, 8: 22, 9: 23, 10: 23, 11: 22, 12: 21, 1: 20, 2: 19, 3: 20}
    if day > biggest_day_for_sign[month]:
        return signs[month]
    return signs[month + 1]


def main():
    print (what_is_my_sign(31, 5))


if __name__ == '__main__':
    main()
