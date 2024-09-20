import copy
import itertools
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
        'F': 10,
        'G': 20,
        'H': 10,
        'I': 35,
        'J': 60,
        'K': 70,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 20,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 17,
        'Y': 20,
        'Z': 21,
    }
    # store offers as a separate dict, could in future calculate saving if subject to change
    offers = {
        'AAA': {'price':130, 'saving':20},
        'AAAAA': {'price':200, 'saving':50},
        'BB': {'price':45, 'saving':15},
        'EEB': {'price':80, 'saving':30},
        'FFF': {'price': 20, 'saving': 10},
        'HHHHH': {'price': 45, 'saving': 5},
        'HHHHHHHHHH': {'price': 80, 'saving': 20},
        'KK': {'price': 120, 'saving': 20},
        'NNNM': {'price': 120, 'saving': 15},
        'PPPPP': {'price': 200, 'saving': 50},
        'QQQ': {'price': 80, 'saving': 10},
        'RRRQ': {'price': 150, 'saving': 30},
        'UUUU': {'price': 120, 'saving': 40},
        'VV': {'price': 90, 'saving': 10},
        'VVV': {'price': 130, 'saving': 20},
    }
    #generate all versions of the combinatorial offer
    combinatorial_offers_dict = generate_combinatorial_offers_dict(
        sample_size = 3,
        items = ['S','T','X','Y','Z'],
        price = 45,
        prices=prices
    )

    offers.update(combinatorial_offers_dict)
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
            #deepcopy is used here to not affect the global variable item counts
            # set a finite but high limit on applications of an offer so as to use offers multiple times
            offer_applied_times = 0
            max_offers_applied = 100
            while offer_applied_times <= max_offers_applied:
                item_counts = remove_offer_from_item_counts(copy.deepcopy(item_counts), offer_items)
                total_price += offer_info['price']
                offer_applied_times +=1
        except ValueError as e:
            continue
    
    for item, price in prices.items():
        if item in item_counts:
            total_price += item_counts[item] * price

    return total_price

def remove_offer_from_item_counts(count: dict, offer: str) -> dict:
    for item in offer:
            if item not in count:
                raise ValueError('item for offer not in cart')
            if count[item] == 0:
                raise ValueError('item for offer not in cart')
            else:
                count[item] -= 1
    return count

def generate_combinatorial_offers_dict(sample_size, items, price, prices):
    combinatorial_offers_dict = {}
    for combination in itertools.combinations_with_replacement(items, sample_size): 
        combination_cost = 0
        for item in combination:
            combination_cost += prices[item]
        saving = combination_cost - price
        offer_key = "".join(combination)
        combinatorial_offers_dict.update(
            {offer_key: {'price': price, 'saving': saving}}
        )
    return combinatorial_offers_dict
