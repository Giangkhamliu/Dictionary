# Write a Python script to sort (ascending and descending) a dictionary by value.
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
a=[]
for value in d.values():
    a.append(value)
    a.sort()
print(a)
print("Ascending:-",a[::-1])
print("Descending:-",a)