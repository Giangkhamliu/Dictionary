my_dict = {'a':50,'b':58,'c':56,'d':40, 'e':100,'f':20}
a=[]
max=0
for i in my_dict:
    a.append(my_dict[i])
    a.sort()
    b=a[:-4:-1]
print("The three higest values are:-",b)
i=0
c=[]
while i<len(b):
    for key, value in my_dict.items():
        if value==b[i]:
          c+=key
    i+=1
print(c)