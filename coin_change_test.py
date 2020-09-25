import coin_change
import unittest


class CoinChangeTest(unittest.TestCase):
    # Run tests for coin_change().

    def test_example_case(self):
        coffee_price = 3.14
        eur_inserted = 500
        change = coin_change.coin_change(coffee_price, eur_inserted)
        condition = change == {2: 248, 0.5: 1, 0.2: 1, 0.1: 1, 0.05: 1, 0.01: 1}
        with self.subTest():
            self.assertTrue(condition, 'Wrong change')

    def test_negative_eur_inserted(self):
        coffee_price = 3.14
        eur_inserted = -1
        change = coin_change.coin_change(coffee_price, eur_inserted)
        condition = change == 'Not enough money inserted'
        with self.subTest():
            self.assertTrue(condition, 'Wrong change')

    def test_negative_coffee_price(self):
        coffee_price = -3.14
        eur_inserted = 10
        change = coin_change.coin_change(coffee_price, eur_inserted)
        condition = change == 'Wrong coffee price'
        with self.subTest():
            self.assertTrue(condition, 'Wrong change')

    def test_decimal_euro_inserted(self):
        coffee_price = 3.14
        eur_inserted = 3.50
        change = coin_change.coin_change(coffee_price, eur_inserted)
        condition = change == {0.2: 1, 0.1: 1, 0.05: 1, 0.01: 1}
        with self.subTest():
            self.assertTrue(condition, 'Wrong change')


if __name__ == '__main__':
    unittest.main()
