# Write a program remove the first key value pair from a nested dictionary.
# Dic= {1: 'NAVGURUKUL',2: 'IN',3:{ 'B' : 'To','C' : 'DHARAMSALA'}}
Dic= {1: 'NAVGURUKUL',2: 'IN',  3:{'A' : 'WELCOME', 'B' : 'To','C' : 'DHARAMSALA'}}
mydic=Dic[3]
mydic1=mydic.pop("A")
print(Dic)