

# Our price table and offers: 
# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+
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
    if skus == "":
        return 0
    #dict store of prices
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
    }
    # store offers as a separate dict, could in future calculate saving if subject to change
    offers = {
        'AAA': {'price':130, 'saving':20},
        'AAAAA': {'price':200, 'saving':50},
        'BB': {'price':45, 'saving':15},
        'EEB': {'price':80, 'saving':30},
    }
    total_price = 0
    item_counts = {}

    #Iter items in basket
    for item in skus:
        if item not in prices:
            return -1
        # Increment count of the item
        item_counts[item] = item_counts.get(item, 0) + 1
    # For each entry in offers, starting with the best saving,
    # attempt to remove the items from the cart and
    # add the offer value to the total
    #sort offers by value
    offers = dict(sorted(offers.items(), key=lambda item: item[1]['saving'], reverse=True))
    for offer_items, offer_info in offers.items():
        try:
            item_counts = remove_offer_from_item_counts(item_counts, offer_items)
            total_price += offer_info['price']
        except ValueError as e:
            continue
    
    for item, price in prices.items():
        total_price += item_counts[item] * price

    return total_price

def remove_offer_from_item_counts(item_counts: dict, offer: str) -> dict:
    for item in offer:
        if item in item_counts:
            if item_counts[item] == 0:
                raise ValueError('item for offer not in cart')
            else:
                item_counts[item] -= 1
    return item_counts
