# Q21.Write a Python program to print all unique values in a dictionary.
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
# {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

dic=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
{"V":"S009"},{"VIII":"S007"}]
# b=[]
# for a in dic:
#     for val in a.values():
#         b.append(val)
# print(set(b))
i=0
b=[]
while i<len(dic):
    for j in dic[i]:
        a=dic[i][j]
        b.append(a)
    i+=1
i=0
c=[]
while i<len(b):
    if b[i] not in c:
        c.append(b[i])
    i+=1
print(c)

    
