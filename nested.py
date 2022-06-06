# [{'S001': {'Adina Park': 85}},
#  {'S002': {'Leyton Marsh': 98}},
#  {'S003': {'Duncan Boyle': 89}},
# {'S004': {'Saim Richards': 92}}]

a=['S001', 'S002', 'S003', 'S004']
b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
c=[85, 98, 89, 92]
x = [{key:value} for key , value in zip(b,c)]
y=[{key:value} for key, value in zip(a,x)]
print(y)
