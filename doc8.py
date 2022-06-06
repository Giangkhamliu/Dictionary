dict={1:10,2:60,3:30,5:50,4:60,5:3}
f={}
for i, j in dict.items():
    if j not in f:
        f[j]=[i]
    else:
        f[j].append(i)
print(f)

# d={"A":1,"a":2}
# print(d["A"])
# print(d["a"])


