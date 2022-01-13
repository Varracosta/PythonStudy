import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-5, -7), 2)
        self.assertEqual(calc.subtract(50, -125), 175)

    def test_multiply(self):
        self.assertEqual(calc.multiply(5, 5), 25)
        self.assertEqual(calc.multiply(8, 7), 56)
        self.assertEqual(calc.multiply(-7, 7), -49)

    def test_divide(self):
        self.assertEqual(calc.divide(4, 2), 2)
        self.assertEqual(calc.divide(81, 9), 9)
        self.assertEqual(calc.divide(8, 2), 4)

        with self.assertRaises(ZeroDivisionError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
