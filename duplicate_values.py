# a={1:1,2:9,3:9,4:16,5:25,6:1,7:9}
# result={}
# for key,value in a.items(): 
#     if value not in result.values():
#         result[key]=value
# print(result)

a= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
u_value = set( val for dic in a for val in dic.values())
print("Unique Values: ",u_value)

