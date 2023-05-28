import random
list = [random.randint(0, 9) for i in range(random.randint(8, 8))]
print(list)
n = int(input("Введите число от 0 до 9:  "))
clos = n
result = list[0]
for i in list:
    if abs(i - n) < clos:
        clos = abs(i - n)
        result = i
print(result)

#list1 = set()
# for unit in range(1, len(list)):
#     if abs(unit - n) <= n:
#         closest = unit
    
# print(closest)
