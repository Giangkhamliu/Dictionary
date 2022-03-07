dic={'Theodore': {'user': 'Theodore', 'age': 45}, 'Roxanne': {'user': 'Roxanne', 'age': 15}, 'Mathew': {'user': 'Mathew', 'age': 21}}
for key,value in dic.items():
    for val in value:
        dic[key]=value[val]

print(dic)