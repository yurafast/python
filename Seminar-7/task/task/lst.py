lst=['1','+', '2']
for i in range(len(lst)):
    if lst[i].isdigit():
        lst[i]=int(lst[i])