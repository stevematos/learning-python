from utils import check_unique


def get_amount_total(sales_orders, filter_symbol_currency='$'):
    amount_total = 0
    for sale_order in sales_orders:
        if sale_order.symbol_currency == filter_symbol_currency:
            amount_total += sale_order.amount
    return amount_total


def verified_one_currency(sales_orders):
    so_currencies = [sales_order.symbol_currency for sales_order in sales_orders]
    return check_unique(so_currencies)

