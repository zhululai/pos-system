import unittest
import pos_system


class TestPosSystem(unittest.TestCase):
    """Class to test the behaviour of the POS system"""

    def test_checkout_function(self):
        codes = ['B', 'A', 'B', 'P', 'B']
        prices = {'A': 25, 'B': 40, 'P': 30}
        self.assertEqual(pos_system.checkout(codes, prices), 155)

    def test_checkout_class(self):
        codes = ['B', 'A', 'B', 'P', 'B']
        prices = {'A': 25, 'B': 40, 'P': 30}
        checkout = pos_system.Checkout(prices)
        for code in codes:
            checkout.scan(code)
        self.assertEqual(checkout.total(), 155)

if __name__ == '__main__':
    unittest.main()
