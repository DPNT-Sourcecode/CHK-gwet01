

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
    item_counts = {}

    #Iter items in basket
    for item in skus:
        if item not in prices:
            return -1
        # Increment count of the item
        item_counts[item] = item_counts.get(item, 0) + 1

    # For each entry in item counts if there's an offer, divide by the offer quantity
    for item, count in item_counts:
        offer = prices[item]['offer']
        if offer:
            num_offers, remainder = divmod(count, offer[0])
            total_price += num_offers * offer[1]
            total_price += remainder * prices[item]['price']
        else:
            total_price += count * prices[item]['price']
    return total_price

