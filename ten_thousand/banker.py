class Banker:
    def __init__(self, balance=0, shelved=0):
        self.balance = balance
        self.shelved = shelved
    def clear_shelf(self):
        self.shelved = 0
    def bank(self):
        self.balance += self.shelved
        amt_deposited = self.shelved
        self.shelved = 0
        return amt_deposited
    def shelf(self, amt):
        self.shelved += amt
if __name__ == '__main__':
    banker=Banker()
    banker.shelf(50)
    print(banker.shelved)