# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально

a = [1, 1, 2, 0, -1, 3, 4, 4]
a = set(a)

print(len(a))

##

a = [1, 1, 2, 0, -1, 3, 4, 4]
unic = 1
for i in range(1, len(a)):
        if a[i] not in a[:i]:
            unic += 1
print(unic)

###
a = [1, 1, 2, 0, -1, 3, 4, 4]
c = 0
v = []
b = 0
for i in a:
    if i not in v:
        c += 1
        v.append(i)
    else: # эту часть можно удалить
        b += 1 # и эту
print(c)


# Задача №19. Общее обсуждение
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

list_1 = [1, 2, 3, 4, 5]
k = 3
print(list_1)
newList = list_1[k:] + list_1[:k] # делаем срезы и меняем местами
print(newList)
##
"""ОТСЮДА И НИЖЕ _ ДОМАШНЕЕ ЗАДАНИЕ
"""
# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]                                     спросить про ключи - идентичные!!
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

Dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
        {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
s = set()
for i in Dict:
    for j in i.values():
        s.add(j)
print(s) # в списке S005 идет с пробелом после значения и без пробела - учитывается как разные знач.

# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

import random
list = [random.randint(0, 9) for i in range(random.randint(8, 20))]
print(list)
pair = 0
#set = ()
for unit in range(1, len(list)):
    if list[unit] > list[unit - 1]:
        print(list[unit] > list[unit - 1]) # не получается вывести значения
        pair += 1
print(pair)


# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел A i
# . Последняя строка содержит число X
import random
list = [random.randint(0, 9) for i in range(random.randint(8, 8))]
print(list)
resalt = 0
n = int(input("Введите число от 0 до 9:  "))
for unit in range(1, len(list)):
    if list[unit] == n:
        resalt += 1
print(resalt)


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел A i
# . Последняя строка
# содержит число X
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
print(result) # решение не полное. Не выведено второе наиболее 
              # близкое число, при условии равенства его с первым.

######



n = int(input())
list_1 = list()
for i in range(n):
    x = int(input())
    list_1.append(x)

k = int(input())
m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)

## еще
# Задача №18. Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
from random import randint

N = int(input("Введите число N: "))
inputList = [randint(1, N) for i in range(N)]
print(inputList)
X = int(input("Введите число X: "))

diffP = 0
oldDiffP = max(inputList)
diffN = 0
oldDiffN = max(inputList)
resNumP = 0
resNumN = 0
for num in inputList:
    diff = X - num

    if diff > 0:
        diffP = diff
    elif diff < 0:
        diffN = diff

    if abs(diffP) < abs(oldDiffP):
        resNumP = num
    oldDiffP = diffP

    if abs(diffN) < abs(oldDiffN):
        resNumN = num
    oldDiffN = diffN
print(resNumP)
print(resNumN)



########



k = int(input())
m = abs(k - list_1[0])  # модуль разности
numbers = []  # список для хранения чисел

for i in range(len(list_1)):
    if abs(list_1[i] - k) <= m:
        if abs(list_1[i] - k) < m:
            numbers = []  # очищаем список, если нашли число ближайшее, чем предыдущее
            m = abs(list_1[i] - k)
        numbers.append(list_1[i])


# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# создать библиотеку, ключи - буквы, содержание - стоимость. делать запрос 
# на стоимость букв в слове и суммировать. Не успеваю...

dict_1 = {'AEIOULNSTRАВЕИНОРСТ': 1, 'DGДКЛМПУ': 2, 'BCMPБГЁЬЯ': 3, 'FHVWYЙЫ': 4, 'KЖЗХЦЧ': 5, 'JXШЭЮ': 8, 'QZФЩЪ': 10} 
word = list(input('Введите слово буквами верхнего регистра: '))
price = 0
for i in word:
    for key in dict_1:
        if i in key:
            price = price + dict_1.get(key)
print(f'Стоимость слова: {price}.')

#####


# Игорь Москалев

onePoints = dict.fromkeys(['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 1)
twoPoints = dict.fromkeys(['Д', 'К', 'Л', 'М', 'П', 'У'], 2)
threePoints = dict.fromkeys(['Б', 'Г', 'Ё', 'Ь', 'Я' ], 3)
fourPoints = dict.fromkeys(['Й', 'Ы'], 4)
fivePoints = dict.fromkeys(['Ж', 'З', 'Х', 'Ц', 'Ч'], 5)
eightPoints = dict.fromkeys(['Ш', 'Э', 'Ю'], 8)
tenPoints = dict.fromkeys(['Ф', 'Щ', 'Ъ'], 10)
mergedDict = onePoints | twoPoints | threePoints | fourPoints | fivePoints | eightPoints | tenPoints 

userText = list(input("Введите одно слово ").upper())
sum = 0
for i in userText:
    sum += mergedDict[i]
print(sum)


###########


eng = "qwertyuiopasdfghjklzxcvbnm"

rus = "йцукенгшщзхъфывапролджэячсмитьбюё"

list_English = {
    1: "AEIOULNSTR",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ",
}
list_Russian = {
    1: "АВЕИНОРСТ",
    2: "ДКЛМПУ",
    3: "БГЁЬЯ",
    4: "ЙЫ",
    5: "ЖЗХЦЧ",
    8: "ШЭЮ",
    10: "ФШЪ",
}

word = input("Введите слово на русском или английском языке: ")

if word[0].lower() in eng:
    summa = 0
    for letter in word:
        for key, value in list_English.items():
            if letter.upper() in value:
                summa += key
    print(f"стоимость введенного английского слова = {summa}")
else:
    if word[0].lower() in rus:
        summa = 0
        for letter in word:
            for key, value in list_Russian.items():
                if letter.upper() in value:
                    summa += key
    print(f"стоимость введенного русского слова = {summa}")