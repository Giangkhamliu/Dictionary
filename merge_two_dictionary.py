#  Write a Python script to merge two Python dictionaries. 
a={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
b={"name":"Grace","age":23}
c={}
for d in (a,b):
    c.update(d)
print(c)