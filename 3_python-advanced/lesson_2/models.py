import random


class SalesOrder:
    def __init__(self, product, price, quantity, symbol_currency='$'):
        self.product = product
        self.price = price
        self.quantity = quantity
        self.symbol_currency = symbol_currency

    @property
    def amount(self):
        return self.price * self.quantity

    @property
    def amount_with_currency(self):
        return f'{self.amount}{self.symbol_currency}'

    def get_shop(self):
        return f'Shop {random.randint(0, 150)}'
