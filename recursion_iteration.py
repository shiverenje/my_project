def replicate_recur(times, data):
    L = []
    if type(times) != int or float and type(data) != int or float or str:
        try:
            if times == 0 or times < 0:
                return L
            else:
                value = replicate_iter(times - 1, data)
                value.append(data)
                return value
        except:
            raise ValueError


def replicate_iter(times, data):
    L = []
    if type(times) != int or float and type(data) != int or float or str:
        try:
            while times > 0:
                L.append(data)
                times -= 1
            return L
        except:
            raise ValueError


print(replicate_recur(2,[]))
print(replicate_iter(2,[]))