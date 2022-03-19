# dic={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
dic = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
a=[]
d={}
for value in dic.values():
    a.append(value)
    a.sort()
print(a)
i=0
while i<len(a):
    for key,value in dic.items():
        if value==a[i]:
            d.update({key:value})
    i+=1
print("The ascending keys and values are:-")
print(d)
e={}
i=-1
while i>=-len(a):
    for key,value in dic.items():
        if value==a[i]:
            e.update({key:value})
    i-=1
print("The descending keys and values are:-")
print(e)

