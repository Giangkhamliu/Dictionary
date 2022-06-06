# d={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# a=[]
# d1={}
# d2={}
# for value in d.values():
#     a.append(value)
# i=0
# b=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[i]<a[j]:
#             b=a[j]
#             a[j]=a[i]
#             a[i]=b
#         j+=1
#     i+=1
# i=0
# j=-1
# while i<len(a):
#     for key, value in d.items():
#         if value==a[i]:
#             d1.update({key:value})
#         elif value==a[j]:
#             d2.update({key:value})
#     j-=1
#     i+=1
# print("Dictionary in ascending order by value:-",d1)
# print("Dictionary in descending order by value:-",d2)


# ###
# # Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# # Dictionary in ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# # Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}
d={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
a=[]
d1=[]
d2={}
for value in d.values():
    a.append(value)
i=0
b=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]<a[j]:
            b=a[j]
            a[j]=a[i]
            a[i]=b
        j+=1
    i+=1
i=0
j=-1
while i<len(a):
    for key, value in d.items():
        if value==a[i]:
            d1.append((key,value))
        elif value==a[j]:
            d2.update({key:value})
    j-=1
    i+=1
print("Dictionary in ascending order by value:-",d1)
print("Dictionary in descending order by value:-",d2)

