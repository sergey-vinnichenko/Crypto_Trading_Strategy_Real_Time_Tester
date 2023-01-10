

# Rounding up cryptocurrency prices
def round_price(value):
    if value > 9999:
        return round(value, 0)
    elif value > 999:
        return round(value, 1)
    elif value > 99.9:
        return round(value, 2)
    elif value > 9.99:
        return round(value, 3)
    elif value > 0.999:
        return round(value, 4)
    elif value > 0.0999:
        return round(value, 5)
    elif value > 0.00999:
        return round(value, 6)
    elif value > 0.000999:
        return round(value, 7)
    else:
        return round(value, 8)