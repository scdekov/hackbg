class Fraction:
    def __init__(self, numerator, denominator):
        self.number = (numerator, denominator)

    def __add__(self, other):
        if self.number[1] == other.number[1]:
            return (self.number[0] + other.number[0], self.number[1])
        else:
            numer = self.number[0] * other.number[1] + self.number[1] * other.number[0]
            denum = self.number[1] * other.number[1]
            return (numer, denum)

    def __sub__(self, other):
        new = Fraction(other.number[0] * (-1), other.number[1])
        return self.__add__(new)

    def __lt__(self, other):
        first = [self.number[0], self.number[1]]
        second = [other.number[0], other.number[1]]
        first[0] *= second[1]
        second[0] *= first[1]
        return first[0] < second[0]

    def __le__(self, other):
        first = [self.number[0], self.number[1]]
        second = [other.number[0], other.number[1]]
        first[0] *= second[1]
        second[0] *= first[1]
        return first[0] == second[0]

    def __gt__(self, other):
        return not(self.__lt__(other) or self.__le__(other))

    def __eq__(self, other):
        return not(self.__lt__(other) or self.__gt__(other))



def main():
    a = Fraction(2, 2)
    b = Fraction(2, 2)
    print(a == b)


if __name__ == '__main__':
    main()
