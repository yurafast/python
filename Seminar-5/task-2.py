# 2. Дан список чисел. Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
    
#     *Пример:* 
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] и т.д.

# Вариант № 1    

# list = [1, 5, 2, 3, 4, 6, 1, 7]
# new_list = []
# new_list.append(list[0])
# temp=list[1]

# for i in range (0, len(list)):
#     if list[i+1] > temp:
#         temp = list[i]
#         new_list.append(temp)

# Вариант № 2

# list = [1, 5, 2, 3, 4, 6, 1, 7]
# new_list = [list[0]]
# max = list[0]
# for i in list:
#     if i > max:
#         new_list.append(i)
#         max = i
# print(new_list)


# Вариант № 3
res=[my_list[0]]
[res.append(item) for item in my_list if item > res[-1]]
print(res)
