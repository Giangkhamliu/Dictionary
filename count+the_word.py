a='Giangkhamliu Grace Pamei'
b={}
i=0
while i<len(a):
    j=0
    c=0
    while j<len(a):
        if a[i]==a[j]:
            c+=1
        j+=1
    b.update({a[i]:c})
    i+=1
print(b)