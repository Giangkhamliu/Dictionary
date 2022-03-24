# 48.Write a Python program to find the length of a given dictionary values.
# {'red': 3, 'green': 5, 'black': 5, 'white': 5}
# 0r
# {'Austin Little': 13, 'Natasha Howard': 14, 'Alfred Mullins': 14, 'Jamie Rowe': 10}

d={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# d={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
d1={}
for i in d.values():
    l=0
    j=0
    while j<len(i):
        l+=1
        j+=1
    d1[i]=l
print(d1)