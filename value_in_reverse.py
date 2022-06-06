dic={'a':[1,2,3,4],'b':[6,7,8,9]}
d={}
a=[]
for i in dic:
    a1=[]
    j=-1
    while j>=-len(dic[i]):
       b=dic[i][j]
       a1.append(b)
       j-=1
    a.append(a1)
    for k in a:
        c=k
    d[i]=c
print(d)




# 0r
dic={'a':[1,2,3,4],'b':[6,7,8,9]}
d={}
a=[]
for i in dic:
    a1=[]
    j=-1
    while j>=-len(dic[i]):
       b=dic[i][j]
       a1.append(b)
       j-=1
    a.append(a1)
    k=0
    while k<len(a):
        c=a[k]
        k+=1
    d[i]=c
print(d)