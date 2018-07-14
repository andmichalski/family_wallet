import unittest

from wallet import Finances


class WalletTests(unittest.TestCase):

    def setUp(self):
        self.incomes = {"Normal": 2000}
        self.expenses = {"home": 500, "car": 200}

    def test_function_split_dict_should_correct_work(self):
        x, y = Finances.split_dict(self.expenses, len(self.incomes))
        self.assertEqual(len(x), 1)
        self.assertEqual(len(y), 1)


if __name__ == "__main__":
    unittest.main()
