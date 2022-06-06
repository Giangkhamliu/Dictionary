# Write a Python program to create a key-value list pairings in a given dictionary.
# A key-value list pairings of the said dictionary:
# [{1: 'Jean Castro'}, {2: 'Lula Powell'}, {3: 'Brian Howell'}, 
# {4: 'Lynne Foster'}, {5: 'Zachary Simon'}]
# and
# [{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]
a={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
res=[]
e=[]
for i,j in a.items():
    for k in j:
        d={i:k}
        a[i]=k
    res.append(d)
e.append(a)
# print(res)
print(e)

