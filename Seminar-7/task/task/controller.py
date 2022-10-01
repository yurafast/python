import input
import lst
import op


def main():
    data = input.input_data()
    lst.work_list(data)
    if data[1] == '+':
        print(f'Result = {op.sum_op(data[0], data[2])}')
    elif data[1] == '-':
        print(f'Result = {op.sub_op(data[0], data[2])}')
    elif data[1] == '*':
        print(f'Result = {op.mul_op(data[0], data[2])}')
    elif data[1] == '/':
        print(f'Result = {op.div_op(data[0], data[2])}')
    else:
        print('Введена не допустимая операция')
