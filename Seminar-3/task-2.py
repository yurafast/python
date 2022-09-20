# '2. Задайте список. Напишите программу, которая определит, 
# 'присутствует ли в заданном списке строк некое число./
sp = []
for i in range(4):
    sp.append(input())

print(sp)

n = int(input())


for i in sp:
    if str(n) in i:
        print('Число есть в элементе списка')
        break
else:
    print('Числа в списке не оказалось')
