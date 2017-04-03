def sum_of_primes(n):
    total = 0

    if not n:
        return 0
    else:
        for num in n:
            if type(num) is int:
                if all(num % y != 0 for y in range(2, num)):
                    if num > 1:
                        #print(num)
                        total += num
            else:
                return 'Invalid Argument'

        return total


l = [31, 6, 43, 9, 59]
print(sum_of_primes(l))
