# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

some_list=[]
n=int(input('введите кол-во элементов в списке: '))

for i in range(n):
    some_list.append(input('введите элемент списка: '))

pro_list = []

for i in range(n//2 + n%2):
    pro_list.append(int(some_list[i]) * int(some_list[len(some_list) - 1 - i]))
print(pro_list)


