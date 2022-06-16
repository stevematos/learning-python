from models import SalesOrder
from functions import get_amount_total, verified_one_currency
from utils import check_unique


# use pytest : requires installing pytest package
def test_is_get_amount_total():
    sales_orders = [
        SalesOrder(
            product='test',
            price=100,
            quantity=2
        )
    ]

    actual = get_amount_total(sales_orders)
    expected = 200
    assert actual == expected

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
    assert actual == expected


def test_verified_one_currency():
    sales_orders = [
        SalesOrder(
            product='test',
            price=100,
            quantity=2
        )
    ]

    actual = verified_one_currency(sales_orders)
    expected = True
    assert actual == expected

    actual = verified_one_currency(sales_orders)
    expected = True
    assert actual == expected

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
    assert actual == expected


def test_check_unique():
    list_unique = ['test', 'test']
    assert check_unique(list_unique)

    list_not_unique = ['test', 'test 1']
    assert not check_unique(list_not_unique)
