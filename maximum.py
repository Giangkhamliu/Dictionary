num={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
max=0
a=[]
for key,value in num.items():
    if value>max:
        max=value
print(key,max)

