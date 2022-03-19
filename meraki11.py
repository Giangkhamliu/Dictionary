# from collections import Counter
# my_dict = {'a':50, 'b':58,'c':56,'d':40, 'e':100, 'f':20}
# k = Counter(my_dict)
# high = k.most_common(3)
# print("Dictionary with 3 highest values:")
# print("Keys: Values")
# for i in high:
#     print(i[0]," :",i[1]," ")



my_dict = {'a':50,'b':58,'c':56,'d':40, 'e':100,'f':20}
a=[]
max=0
for i in my_dict:
    a.append(my_dict[i])
    a.sort()
    b=a[:-4:-1]
print("The three higest values are:_",b)




