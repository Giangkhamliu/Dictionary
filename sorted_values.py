d={"Ring":"1500", "Grace":"1200","Jian":"1700","Lan":"1600"}
a=sorted(d.values())
dict={}
for i in a:
    for j in d.keys():
        if d[j]==i:
            dict[j]=d[j]
print(dict)