lst = ['1', '+' , '5j' , '-' , '5', '+' , '7j']
for i in range(len(lst), 2):
    if i == 2 or i == 6:
        lst[i]=lst[i: -1]

    print(lst[i])
x = lst[:3]
y = lst[4:]
print (x,y)
a=complex(lst[0], lst[2])
b=complex(lst[4], lst[-1])
print(a,b)