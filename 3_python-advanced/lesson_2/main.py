from models import SalesOrder
from functions import get_amount_total, verified_one_currency

sales_orders = [
    SalesOrder(
        product='MacBook pro m1',
        price=3200,
        quantity=2
    ),
    SalesOrder(
        product='Laptop Lenovo',
        price=1200,
        quantity=1
    )
]


print(verified_one_currency(sales_orders))

sales_orders.append(
    SalesOrder(
        product='Mouse Razer',
        price=600,
        quantity=1,
        symbol_currency='S/.'
    )
)


amount_total = get_amount_total(sales_orders)
print(amount_total)

amount_total = get_amount_total(sales_orders, filter_symbol_currency='S/.')
print(amount_total)

print(verified_one_currency(sales_orders))

