

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus) -> int:
    """
    Calculates the total price of a given list of items
    Param:
        skus (str): A string containing the SKUs of all products in the basket
    Returns:
        total_price (int): The total price ofall items, or -1 if the input is invalid.
    """

    #dict store of prices
    prices = {
        'A': {'price': 50, 'offer': (3, 130)},
        'B': {'price': 30, 'offer': (2, 45)},
        'C': {'price': 20, 'offer': None},
        'D': {'price': 15, 'offer': None},
    }
    total_price = 0


    return total_price

