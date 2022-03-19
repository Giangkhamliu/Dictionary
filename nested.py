##{'S001': {'Saim Richards': 85}, 
# 'S002': {'Saim Richards': 85}, 
# 'S003': {'Saim Richards': 85}, 
# 'S004': {'Saim Richards': 85}}

l1=['S001', 'S002', 'S003', 'S004']
l2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
l3=[85, 98, 89, 92]
d={}
k=0
for i in l1:
    for j in l2:
        d[i]={}
        d[i][j]=l3[k]
print(d)