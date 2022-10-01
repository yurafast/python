# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

some_list=[]
n=int(input('введите кол-во элементов в списке: '))

for i in range(n):
    some_list.append(input('введите элемент списка: '))

print(some_list)
summ=0

for i in range (1,len(some_list),2):
    summ = summ + int(some_list[i])
print(summ)