# Напишите программу, которая принимает натуральное число N и выводит числа от -N До N
number = int(input('введите число '))
start = -number
while start <= number:
    print(start, sep='(_|_)')
    start += 1
