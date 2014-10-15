class Cash_desk(object):
    def __init__(self):
        self.money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    def take_money(self, money_to_take):
        for el in money_to_take:
            self.money[el] += money_to_take[el]

    def total(self):
        sum = 0
        for el in self.money:
            sum += el * self.money[el]
        return sum

    def _rec(self, money_arr, summ):
        flag = False
        if summ == 0:
            flag = True
        else:
            for i in range(summ):
                for el in money_arr:
                    if summ - el >= 0:
                        money_arr.remove(el)
                        return self._rec(money_arr, summ - el)
        return flag

    def can_withdraw_money(self, summ):
        money_arr = []
        for el in self.money:
            for i in range(0, self.money[el]):
                money_arr.append(el)
        money_arr = sorted(money_arr)
        money_arr = money_arr[::-1]
        return self._rec(money_arr, summ)


def main():
    my_cash_desk = Cash_desk()
    my_cash_desk.take_money({1: 2, 50: 1, 20: 1})
    print (my_cash_desk.total())
    print (my_cash_desk.can_withdraw_money(30))
    print (my_cash_desk.can_withdraw_money(70))


if __name__ == '__main__':
    main()
