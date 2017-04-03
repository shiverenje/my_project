class BankAccount(object):
    def deposit(self):
        pass

    def withdraw(self):
        pass

    balance = 0


class SavingsAccount(BankAccount):
    def __init__(self):
        self.balance = 500

    def deposit(self, deposit):
        if deposit > 0:
            self.balance += deposit
            return self.balance
        else:
            return 'Invalid deposit amount'

    def withdraw(self, withdrawal):
        if self.balance - withdrawal < 500:
            print('Cannot withdraw beyond tyhe minimum account balance')
        elif withdrawal > self.balance:
            print('Cannot withdraw beyond the minimum account balance')
        elif withdrawal < 0:
            return 'Invalid withdraw amount'
        else:
            self.balance -= withdrawal
            return self.balance


class CurrentAccount(BankAccount):
    def __init__(self):
        self.balance = 0

    def deposit(self, cash_deposit):
        if cash_deposit > 0:
            self.balance += cash_deposit
            return self.balance
        else:
            return 'Invalid deposit amount'

    def withdraw(self, withdrawal):
        if withdrawal < 0:
            return 'Invalid withdraw amount'
        elif self.balance - withdrawal < 0:
            print('Cannot withdraw beyond the current account balance')
        else:
            self.balance -= withdrawal
            return self.balance


test1 = SavingsAccount()
print(test1.withdraw(400))
print(test1.withdraw(200))

test2 = CurrentAccount()
print(test2.deposit(500))
print(test2.withdraw(-400))
print(test2.withdraw(400))
