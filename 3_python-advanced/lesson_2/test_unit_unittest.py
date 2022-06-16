import unittest

from models import SalesOrder
from functions import get_amount_total, verified_one_currency


# use unittest
class TestFunctions(unittest.TestCase):

    def test_get_amount_total(self):
        sales_orders = [
            SalesOrder(
                product='test',
                price=100,
                quantity=2
            )
        ]

        actual = get_amount_total(sales_orders)
        expected = 200
        self.assertEqual(actual, expected)

        # append SalesOrder for tests
        sales_orders.append(
            SalesOrder(
                product='test soles',
                price=200,
                quantity=3,
                symbol_currency='S/.'
            )
        )
        actual = get_amount_total(sales_orders, filter_symbol_currency='S/.')
        expected = 600
        self.assertEqual(actual, expected)

    def test_verified_one_currency(self):
        sales_orders = [
            SalesOrder(
                product='test',
                price=100,
                quantity=2
            )
        ]

        actual = verified_one_currency(sales_orders)
        expected = True
        self.assertEqual(actual, expected)

        sales_orders = [
            SalesOrder(
                product='test dollars 1',
                price=100,
                quantity=1
            ),
            SalesOrder(
                product='test dollars 2',
                price=200,
                quantity=2
            )
        ]

        actual = verified_one_currency(sales_orders)
        expected = True
        self.assertEqual(actual, expected)

        sales_orders.append(
            SalesOrder(
                product='test soles 1',
                price=100,
                quantity=2,
                symbol_currency='S/.'
            )
        )
        actual = verified_one_currency(sales_orders)
        expected = False
        self.assertEqual(actual, expected)


