a = 8
b = 5
def SumRec(a, b):
    if b == 0:
        return (a)
    elif b > 0:
        return SumRec(a + 1, b - 1)
    else:
        return SumRec(a - 1, b + 1) # если b<0
print(SumRec(a, b))