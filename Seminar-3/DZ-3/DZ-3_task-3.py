# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

some_list=[]

n=int(input('введите кол-во элементов в списке: '))

for i in range(n):
    some_list.append(input('введите элемент списка: '))
print(some_list)

target_list=[]
for i in range (len(some_list)):
    if '.' in some_list[i]:
        target_list[i]=int(some_list.split('.')[1])
print(target_list)