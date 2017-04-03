def culate(amount, time, rate):
    check = (int, float)
    if isinstance(amount, check) or isinstance(rate, check) or isinstance(time, check):
        if time <= 12:
            loan = amount * rate * time
            amount_repaid = amount + loan
            return amount_repaid
        else:
            raise ValueError

# a = input('Enter the amount')
# t = input('enter the time')
# r = input('enter the rate')

# print(culate(a, t, r))
# if __name__ = '__main__':
# print loan_calculator(100000,1,0.12)
