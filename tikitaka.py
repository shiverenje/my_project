#print(3 in [1,3,5])

#for x in 'andela'[::-1]:
        #print(x*2)

def  s(a):
    largest = 0
    smallest =0
    if a[1]>a[0]:
        largest = a[1]
    if a[1]<a[0]:
        smallest = a[0]
    for i in a:
        res=largest//smallest
    return res

a = [9,5,1,2,4,3]
print(s(a))