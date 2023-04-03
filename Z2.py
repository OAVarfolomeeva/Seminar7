#Определить индексы элементов массива (списка),
#значения которых принадлежат заданному диапазону
#(т.е. не меньше заданного минимума и не больше заданного максимума)

import random

massive=[]

n=int(input("Размерность массива: "))

for k in range(1,n+1):
    massive.append(random.randint(1,20))

print(massive)

k=int(input("Минимальное значение "))
d=int(input("Максимальное значение "))
print(*[i for i in range(len(massive)) if k <= massive[i] <= d])
