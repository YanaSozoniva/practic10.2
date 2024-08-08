def calculate_taxes(prices: list[float], tax_rate: float) -> list[float]:
    """Функция вычисляет стоимость товаров с учётом налога."""

    if tax_rate < 0:
        raise ValueError('Неверный налоговый процент')

    taxed_prices = []

    for price in prices:
        if price <= 0:
            raise ValueError('Неверная цена')
        tax = price * tax_rate / 100
        taxed_prices.append(price + tax)

    return taxed_prices


def calculate_tax(price: float, tax_rate: float, *, discount: float = 0, accuracy: int = 2) -> float:
    """Функция вычисляет стоимость товаров с учётом налога и скидки."""

    for arg in [price, tax_rate, discount, accuracy]:
        if not isinstance(arg, (float | int)):
            raise TypeError("Ошибка типа")

    if price < 0:
        raise ValueError('Неверная цена')

    if tax_rate < 0 or tax_rate >= 100:
        raise ValueError('Неверный налоговый процент')

    tax = price * tax_rate / 100 + price
    discount_price = tax * discount / 100

    return round(tax - discount_price, accuracy)
