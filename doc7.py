# Q44.Write a Python program to split a given dictionary of lists into list of dictionaries.
# Original dictionary of lists:
d= {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
res=[]
d1={}
a,b=d.values()
i=0
while i<len(a):
    for j,k in d.items():
        d1={j:k[i]}
        res.append(d1)
    i+=1
print(res)
    
    


# op=[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language':
# 84}, {'Science': 95, 'Language': 80}]