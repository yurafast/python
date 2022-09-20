# 1. Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный. 
#     *Пример:*   
#     2+2 => 4; 
#     1+2*3 => 7; 
#     1-2*3 => -5;
#     - Добавьте возможность использования скобок, меняющих приоритет операций.    
#         *Пример:*   
#         1+2*3 => 7; 
#         (1+2)*3 => 9;

user_str = '12+23' 

#print(eval(user_str))

def f(function, a, b):
    return function(a, b)


def equation(string: str):
    if string == '+':
        return lambda a, b: a + b
    elif string == '*':
        return lambda a, b: a * b
    elif string == '/':
        return lambda a, b: a / b
    elif string == '-':
        return lambda a, b: a - b


sign = []

for i in user_str:
    if i in '+-/*':
        sign.append(i)
print(sign)

if len(sign) == 1:
    index = user_str.find(sign[0])
    a = int(user_str[:index])
    b = int(user_str[index + 1 : len(user_str)])
    res = f(equation(sign[0]), a, b)
else:


# for i in sign:
#     if i == '*':
#         index = user_str.find('*')
#         a = int(user_str[user_str.find('+') + 1 : index])
#         b = int(user_str[index + 1 : len(user_str)])
#         res = f(lambda a, b: a * b, a, b)
print(res)
# print(user_str)
