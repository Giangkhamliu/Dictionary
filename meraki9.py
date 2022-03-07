# Store the unique letters and their frequency of the letters from 
# the word "MISSISSIPPI" to a dictionary, were the letters are the keys 
# and their frequencies are the values.
# output-{'M':1,'I':4,'S':4,'P':2}
dic="MISSISSIPPI"
i=0
d={}
while i<len(dic):
    j=0
    c=0
    while j<len(dic):
        if dic[i]==dic[j]:
            c=c+1
        j=j+1
    d.update({dic[i]:c})
    i=i+1
print(d)
