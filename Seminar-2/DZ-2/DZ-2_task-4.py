# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.






from random import *
n=int(input('Введите число: '))

some_list = [randint(-n,n) for _ in range(randint(5,10))]
print(some_list)


f = open ('17.txt', 'w')
for i in range(randint(2, len(some_list))):
    f.write(str(randint(0, len(some_list) - 1)) + '\n')
f.close()

proizved = 1

with open ('17.txt', 'r') as f:
    for i in f.read().splitlines():
        print(i)
    proizved = proizved * some_list[int(i)] 
print(proizved)    