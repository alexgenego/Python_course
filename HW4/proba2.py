import random
N = int(input("Введите количество кустов: "))
numbers = list(range(1, N+1))
print(numbers)
NewBush = list(numbers)
random.shuffle(NewBush)
print(NewBush)
SumBush = []
for i in range(len(NewBush)):
    if i < N-1:
        SumBush.append(NewBush[i-1] + NewBush[i] + NewBush[i+1])
    else: SumBush.append(NewBush[i-1] + NewBush[i] + NewBush[1])
print(SumBush)
max_harvest = max(SumBush)
ind = SumBush.index(max_harvest)
print(ind)
if N - ind > 1:
    print(f'сместиться на {N-ind-1} куста в сторону увеличения номеров')
elif N - ind == 1:
    print("собираем урожай с этого куста и соседних справа и слева")
else: print ("шаг назад")