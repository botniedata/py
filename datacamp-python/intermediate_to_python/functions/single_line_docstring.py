def calculate_discount(price, discount_percent=15, round_result=True):
    # Add a single-line docstring
    """Calculate the discounted price of a product."""

    discount_price = price - (price * (discount_percent / 100))
    if round_result == True:
        return round(discount_price, 2)
    else:
        return discount_price
    
# Access the docstring
print(calculate_discount.__doc__)