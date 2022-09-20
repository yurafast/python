# 2. Дана последовательность чисел. Получить список уникальных элементов 
# заданной последовательности.

# *Пример:* 

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

user_list=[1, 2, 3, 5, 1, 5, 3, 10]

# Вариант 1

# result_list = []

# for i in user_list:
#     count = 0
#     for k in user_list:
#         if i == k:
#             count += 1
#     if count == 1:
#         result_list.append(i)

# print(result_list)

# Вариант 2
# result_list_2 =[]
# for i in user_list:
#     if user_list.count(i) == 1:
#         result_list_2.append(i)

# result_list = [i for i in user_list if user_list.count(i) == 1]

# print(result_list)

Вариант 3

my_list = [1,2,3,4,4,6,5,6,7]

print(tuple(filter (lambda num: my_list.count(num)==1,my_list)))