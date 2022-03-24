# Write a Python program to convert a given list of lists to a dictionary.
# Convert the said list of lists to a dictionary:
# {1:['Jean Castro','V'],2:['Lula Powell','V'],3:['Brian Howell','VI'],4: ['Lynne Foster', 'VI'],
#  5:['Zachary Simon', 'VII']}
l=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4,'Lynne Foster','VI'],
[5,'Zachary Simon', 'VII']]
i=0
dic={}
d=[]
while i<len(l):
    e=[]
    b=l[i][0]
    j=0
    while j<len(l[i]):
        if l[i][j]!=l[i][0]:
            a=l[i][j]   
            e.append(a)
        j+=1
    d.append(e)
    k=0
    while k<len(d):
        g=d[k]
        k+=1
    dic[b]=g
    i+=1
print(dic)

