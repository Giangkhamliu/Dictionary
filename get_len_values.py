a={'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
# Total length of all values of the said dictionary with string values:
# 20
count=0
for value in a.values():
    for val in value:
        count+=1
print(count)