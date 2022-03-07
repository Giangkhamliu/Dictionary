# rec = {"Name" : "Python", "Age":"20","Addr" : "NJ", "Country" :"USA"}
# id1 = id(rec)
# del rec
# rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
# id2 = id(rec)
# print(id1 == id2)

# details={"name":"Grace","age":12,"email":"grace21@navgurukul.org",}
# print(details["name"])
# print(details["email"])
# print(details["age"])


# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for x,y in dict1.items():
#     sum=sum+y
# print(sum)

# c=dict()
# for i in range(1,16):
#     c[i]=i*i
# print(c)

# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}
# c={}
# for i in (s,a):
#     c.update(i)
# print(c)



ini_dict = {'a' : 'akshat', 'b' : 'bhuvan', 'c': 'chandan'}
print("intial_dictionary", str(ini_dict))
keys = ini_dict.keys()
values = ini_dict.values()
print ("keys : ", str(keys))
print ("values : ", str(values))
# Output:
# intial_dictionary {'a': 'akshat', 'b': 'bhuvan', 'c': 'chandan'}
# keys :  dict_keys(['a', 'b', 'c'])
# values :  dict_values(['akshat', 'bhuvan', 'chandan'])
 

ini_dict = {'a' : 'akshat', 'b' : 'bhuvan', 'c': 'chandan'}
print("intial_dictionary", str(ini_dict))
keys, values = zip(*ini_dict.items())
print ("keys : ", str(keys))
print ("values : ", str(values))
# Output:
# intial_dictionary {'a': 'akshat', 'c': 'chandan', 'b': 'bhuvan'}
# keys :  ('a', 'c', 'b')
# values :  ('akshat', 'chandan', 'bhuvan')
 
# Method #3: Using items()
ini_dict = {'a' : 'akshat', 'b' : 'bhuvan', 'c': 'chandan'}
print("intial_dictionary", str(ini_dict))
keys = []
values = []
items = ini_dict.items()
for item in items:
    keys.append(item[0]), values.append(item[1])
print ("keys : ", str(keys))
print ("values : ", str(values))
# Output:
# intial_dictionary {'b': 'bhuvan', 'c': 'chandan', 'a': 'akshat'}
# keys :  ['b', 'c', 'a']
# values :  ['bhuvan', 'chandan', 'akshat']



