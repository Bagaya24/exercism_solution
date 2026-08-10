"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    items = []
    for item in items_to_add:
        if item not in items:
            if item in current_cart.keys():
                current_cart[item] += items_to_add.count(item)
            else:
                current_cart[item] = items_to_add.count(item)
        items.append(item)
    return current_cart
        


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    inventory = {}
    for note in notes:
        inventory.setdefault(note, notes.count(note))
    return inventory


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    new_dict = dict(recipe_updates)
    ideas.update(new_dict)
    return ideas
    


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    new_dict = dict(sorted(cart.items()))
    return new_dict


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    new_dict = {}
    for key, value in aisle_mapping.items():
        if key in cart.keys():
            value.insert(0, cart[key])
            new_dict[key] = value
    return dict(reversed(dict(sorted(new_dict.items())).items()))


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    new_fulfillement_cart = dict(sorted(fulfillment_cart.items()))
    new_store_inventory = dict(sorted(store_inventory.items()))
    for key, value in new_fulfillement_cart.items():
        if new_store_inventory[key][0] <= value[0]:
            new_fulfillement_cart[key][0] = "Out of Stock"
        else:
            value[0] = new_store_inventory[key][0] - value[0] 
    store_inventory.update(new_fulfillement_cart)
    return store_inventory