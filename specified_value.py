def check(dict,val):
    a=[]
    for key,value in dict.items():
        if value==val:
            a.append(key)
    print(a)
dict= {
  'Theodore': 19,
  'Roxanne': 20,
  'Mathew': 21,
  'Betty': 20      
}
check(dict,20)
