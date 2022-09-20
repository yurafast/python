# 1. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 1 2 3 5

with open ('seminar5.txt', 'w') as f1:
    f1.write('1 2 3 5')

with open ('seminar5.txt', 'r') as f1:
    line1=list(f1.read().split())
    print(line1)

for i in range (1,len(line1)):
    if int(line1[i])-1 !=int(line1[i-1]):
        print(int(line1[i])-1)

# Вариант решения № 2

# path_1 = 'task1.txt'

# def read_file(path):
#     out_string = ''
#     res_txt = open(path, 'r')
#     out_string = res_txt.read()
#     res_txt.close()
#     out_list = out_string.split()

#     for i in range(0, len(out_list)):
#         out_list[i] = int(out_list[i])

#     return out_list

# def find_number(input_list: list):
    
#     for i in range(1, len(input_list)):
#         if input_list[i] - 1 != input_list[i - 1]:
#             number = input_list[i - 1] + 1
#             break
#     return number


# print(f'Не хватает числа {find_number(read_file(path_1))}')


# Вариант № 3

my_list = [1, 2, 4, 5, 6, 8, 9, 11]

res = [(my_list[i] - 1) for i in range(1, len(my_list)) if (my_list[i] - 1) != my_list[i - 1]]
print(res)
