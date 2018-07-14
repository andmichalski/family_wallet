class Finances():

    def __init__(self):
        incomes = {}
        with open("incomes.txt") as f:
            for line in f:
                a = line.split()
                incomes[a[0]] = int(a[1])
        self.incomes = incomes

        expenses = {}
        with open("expenses.txt") as f:
            for line in f:
                a = line.split()
                expenses[a[0]] = int(a[1])
        self.expenses = expenses

    def calculate_finances(incomes, expenses):
        finances_sum = sum(incomes.values()) - sum(expenses.values())
        return finances_sum

    def split_dict(ndict, length):
        d1, d2 = {}, {}
        i = 0
        for key, value in ndict.items():
            if i < length:
                d1[key] = value
            else:
                d2[key] = value
            i += 1
        return d1, d2

    def show_finances(self):
        incomes = self.incomes
        expenses = self.expenses
        print(f'{"Incomes":^20} | {"Expenses":^20}')
        if len(incomes) < len(expenses):
            exp1, exp2 = Finances.split_dict(expenses, len(incomes))
            zipped = zip(incomes, exp1)
            for key_inc, key_exp in zipped:
                print(f'{key_inc:7s} - {incomes[key_inc]:7d} zl | {key_exp:7s} - {expenses[key_exp]:7d} zl')
            for key_exp, val_exp in exp2.items():
                print(f'{"":20s} | {key_exp:7s} - {val_exp:7d} zl')
            print("-" * 43)
            print(f'{"Sum ":7s} {sum(incomes.values()):9d} zl | {sum(expenses.values()):17d} zl')
            print(f'Diffrence: {sum(incomes.values())-sum(expenses.values()):6d} zl')
        elif len(incomes) > len(expenses):
            inc1, inc2 = Finances.split_dict(incomes, len(expenses))
            zipped = zip(inc1, expenses)
            for key_inc, key_exp in zipped:
                print(f'{key_inc:7s} - {incomes[key_inc]:7d} zl | {key_exp:7s} - {expenses[key_exp]:7d} zl')
            for key_inc, val_inc in inc2.items():
                print(f'{key_inc:7s} - {val_inc:7d} zl | {"":20s}')
            print("-" * 43)
            print(f'{"Sum ":7s} {sum(incomes.values()):9d} zl | {sum(expenses.values()):17d} zl')
            print(f'Diffrence: {sum(incomes.values())-sum(expenses.values()):6d} zl')
        else:
            zipped = zip(incomes, expenses)
            for key_inc, key_exp in zipped:
                print(f'{key_inc:7s} - {incomes[key_inc]:7d} zl | {key_exp:7s} - {expenses[key_exp]:7d} zl')
            print("-" * 43)
            print(f'{"Sum ":7s} {sum(incomes.values()):9d} zl | {sum(expenses.values()):17d} zl')
            print(f'Diffrence: {sum(incomes.values())-sum(expenses.values()):6d} zl')


def main():
    Finances().show_finances()


if __name__ == "__main__":
    main()
