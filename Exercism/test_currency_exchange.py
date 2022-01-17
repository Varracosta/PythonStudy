import unittest
import currency_exchange


class TestCurrencyExchange(unittest.TestCase):

    def test_exchangeable_value(self):
        self.assertEqual(currency_exchange.exchangeable_value(470000, 1050, 30, 10000000000), 0)
        self.assertEqual(currency_exchange.exchangeable_value(470000, 0.00000009, 30, 700), 4017094016600)
        self.assertEqual(currency_exchange.exchangeable_value(425.33, 0.0009, 30, 700), 363300)
