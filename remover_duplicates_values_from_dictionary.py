d1={'exterior':["blue","blue","green"],"interior":["leather","cloth","leather"]}
d2={}
for k,v in d1.items():
    d2[k]=set(v)
print(d2)