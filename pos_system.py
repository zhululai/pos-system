class Item:
    """Class to represent an item sold by the supermarket"""

    def __init__(self, name, code, offer):
        self._name = name
        self._code = code
        self._offer = offer

    def get_name(self):
        return self._name

    def get_code(self):
        return self._code

    def get_offer(self):
        return self._offer


class Inventory:
    """Class to represent the inventory of the supermarket"""

    def __init__(self):
        self._items = dict()

    def add_item(self, item):
        code = item.get_code()
        self._items[code] = item

    def remove_item(self, code):
        del self._items[code]

    def find_item(self, code):
        return self._items[code]


# Initialize the inventory of the supermarket
inventory = Inventory()
apple = Item('Apple', 'A', lambda n, p: n // 3 * 2 * p + n % 3 * p)
banana = Item('Banana', 'B', lambda n, p: n // 3 * 100 + n % 3 * p)
pear = Item('Pear', 'P', lambda n, p: n * p)
inventory.add_item(apple)
inventory.add_item(banana)
inventory.add_item(pear)


def checkout(codes, prices):
    """Function for customers to check out of their items"""

    numbers = dict()
    for code in set(codes):
        numbers[code] = 0
    for code in codes:
        numbers[code] += 1
    total = 0
    for code in set(codes):
        offer = inventory.find_item(code).get_offer()
        total += offer(numbers[code], prices[code])
    return total


class Checkout:
    """Class for customers to check out of their items"""

    def __init__(self, prices):
        self._prices = prices
        self._codes = list()

    def scan(self, code):
        self._codes.append(code)

    def total(self):
        return checkout(self._codes, self._prices)
