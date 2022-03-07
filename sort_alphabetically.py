num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
for key,value in num.items():
    a=(sorted(value))
    num[key]=a
print(num)


