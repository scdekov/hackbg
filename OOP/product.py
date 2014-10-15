class Product:
    def __init__(self, name, stock_price, final_price):
        self.name = name
        self. stock_price = stock_price
        self. final_price = final_price

    def profit(self):
        return self.final_price - self.stock_price


class Laptop(Product):
    def __init__(self, name, stock_price, final_price, discspace, RAM):
        super().__self__(name, stock_price, final_price)
        self.discspace = discspace
        self.RAM = RAM


class Smartphone(Product):
    def __init__(self, name, stock_price, final_price, display_size, mega_pixels):
        super().__init__(name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store():
    def __init__(self, name):
        self.name = name
        self.products = {}
        self.profit = 0

    def load_new_products(self, product, count):
        self.products[product] = count

    def list_products(self, product_class):
        for el in self.products:
            if isinstance(el, type(product_class)):
                print (el.name + " - ", self.products[el])

    def sell_product(self, product):
        for el in self.products:
            if isinstance(el, type(product)) and self.products[el] > 0:
                self.products[el] -= 1
                self.profit += el.profit()
                return True
        return False

    def total_income(self):
        return self.profit


def main():
    store = Store('Laptop.bg')
    smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
    store.load_new_products(smarthphone, 2)
    store.list_products(smarthphone)
    print (store.sell_product(smarthphone))  # True
    print (store.sell_product(smarthphone))  # True
    print (store.total_income())  # 640


if __name__ == '__main__':
    main()
