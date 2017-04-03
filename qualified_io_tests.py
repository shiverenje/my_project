def fizz_buzz(n):
    if n > 0:
        if n % 5 == 0 and n % 3 != 0:
            return 'buzz'
        elif n % 3 == 0 and n % 5 != 0:
            return 'fizz'
        elif n % 5 == 0 and n % 3 == 0:
            return ('fizzBuzz')
        else:
            return n
    else:
        return 'Invalid argument'


print(fizz_buzz(30))


