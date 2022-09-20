# Задайте строки из набора чисел
# Напишите программу, которая покажет наибольшее и наименьшее число. В качестве разделителя, пробел.


# stroka = input(' введите строку чисел: ')
# stroka=stroka.split()

# spisok_cisel = []
# for i in stroka:
#     spisok_cisel.append(int(i))
# print(spisok_cisel)

# print(f'{min(spisok_cisel)} , {max(spisok_cisel)}')

some_str=input() # '1 2 3 4 5'
some_list=some_str.split()
some_int_list = list(map(int, some_list))
print(max(some_int_list), min(some_int_list))