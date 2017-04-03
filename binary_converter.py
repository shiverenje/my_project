def binary_converter(n):
    kit = ' '
    if type(n) is int or type(n) is float:
        if n == 0:
            return 0
        elif n<0:
            return 'Input below 0 not allowed'
        elif n > 255:
            return 'Input above 255 not allowed'
        else:
            while 1 <= n <= 255:
                y = divmod(n, 2)
                n, x = y[0], y[1]
                kit += str(x)
                r = kit[::-1]
            return r
    else:
        return 'Invalid input'


def binary_converte(n):
    if n == 0:
        return "0"
    elif n < 0:
        return "Input below 0 not allowed"
    elif n > 255:
        return "Invalid input"
    else:
        ans = ""
        while n > 0:
            temp = n % 2
            ans = str(temp) + ans
            n = n / 2
        return ans


print(binary_converter(300))

#print(binary_converte(5))
