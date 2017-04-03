def num_word(n):
    if n == 1:
        return 'One'
    elif n == 2:
        return 'Two'
    elif n == 3:
        return 'Three'
    elif n == 4:
        return 'Four'
    elif n == 5:
        return 'Five'
    elif n == 6:
        return 'Six'
    elif n == 7:
        return 'seven'
    elif n == 8:
        return 'Eight'
    elif n == 9:
        return 'Nine'
    else:
        return 'Not number'


def num(n):
    d = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    for k, v in d.items():
        if n == k:
            return v


print(num_word(6))
print(num(8))
