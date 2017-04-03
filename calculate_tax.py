

def calculate_tax(sal):
    L = dict()
    test = L.values()

    if isinstance(sal,dict):
        try:
            for i in sal:
                f = sal[i]
                if 0 <= f <= 1000:
                    value = f - 0
                    tax1 = value * 0
                    test = tax1
                    L[i] = test
                elif 1001 <= f <= 10000:
                    value = f - 1000
                    tax1 = (1000 - 0) * 0
                    tax2 = value * 0.1
                    test = tax1 + tax2
                    L[i] = test
                elif 10001 <= f <= 20200:
                    value = f - 10000
                    tax1 = (1000 - 0) * 0
                    tax2 = (10000 - 1000) * 0.1
                    tax3 = value * 0.15
                    test = tax1 + tax2 + tax3
                    L[i] = test
                elif 20201 <= f <= 30750:
                    value = f - 20200
                    tax1 = (1000 - 0) * 0
                    tax2 = (10000 - 1000) * 0.1
                    tax3 = (20200 - 10000) * 0.15
                    tax4 = value * 0.2
                    test = tax1 + tax2 + tax3 + tax4
                    L[i] = test
                elif 30751 <= f <= 50000:
                    value = f - 30750
                    tax1 = (1000 - 0) * 0
                    tax2 = (10000 - 1000) * 0.1
                    tax3 = (20200 - 10000) * 0.15
                    tax4 = (30750 - 20200) * 0.2
                    tax5 = value * 0.25
                    test = tax1 + tax2 + tax3 + tax4 + tax5
                    L[i] = test
                elif f > 50000:
                    value = f - 50000
                    tax1 = (1000 - 0) * 0
                    tax2 = (10000 - 1000) * 0.1
                    tax3 = (20200 - 10000) * 0.15
                    tax4 = (30750 - 20200) * 0.2
                    tax5 = (50000 - 30750) * 0.25
                    tax6 = value * 0.3
                    test = tax1 + tax2 + tax3 + tax4 + tax5 + tax6
                    L[i] = test
                else:
                    pass
            return L

        except (AttributeError,TypeError):
            raise ValueError("The provided input is not a dictionary")
    else:
        raise ValueError('Invalid input of type int not allowed')


val={"James": 20500, "Mary": 500, "Evan": 70000}
val2 = {}
res  = calculate_tax(val2)
print(res)
