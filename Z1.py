""" Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
 """


n = int(input('Введите количество элементов: '))
a = [0]*n
a[0] = int(input('Введите первый элемент прогрессии: '))
d = int(input('Введите разность прогрессии: '))
for i in range(1,n):
    a[i]= a[i-1]+d
    print(a[i])




""" n = int(input('Введите количество элементов первого списка: '))
spisokn = list(map(int, input(f'Введи {n} цифр через пробел: ').split()))
if len(spisokn) == n:
    m = int(input('Введите количество элементов второго списка: '))
    spisokm = list(map(int, input(f'Введи {m} цифр через пробел: ').split()))
    if len(spisokm) == m:
        c = list(set(spisokn) & set(spisokm))
        print(f'Числа, которые встречаются в обоих списках {c}') 
    else:
         print('Введенные элементы не соответствуют заявленному количеству!')   
else:
    print('Введенные элементы не соответствуют заявленному количеству!')

massive=[]

n=int(input("Размерность массива > "))

for k in range(1,n+1):
    massive.append(random.randint(1,9))

print(massive)

x = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
min = abs(x - massive[0])
index = 0
for i in range(1, n):
        count = abs(x - massive[i])
        if count < min:
            min = count
            index = i
print(f'Число {massive[index]} в массиве наиболее близко по величине к числу {x}')


 """