import unittest

from wallet import Finances

class WalletTests(unittest.TestCase):

    def setUp(self):

        self.incomes = {"PIG": 2000, "CERVI": 3000}
        self.expenses = {"home": 500, "car": 200, "food": 800}

    def test_show_finances_should_work(self):
        print(Finances.show_finances(self.incomes, self.expenses))

    def test_split_dict(self):
        x, y = Finances.split_dict(self.expenses,2)
        print(x ,y)

if __name__ == "__main__":
    unittest.main()