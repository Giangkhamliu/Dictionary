person={'name':'jack','age':20,'gender':{'male','female'},4:{'organisation':'navgurukul','place':'dharamsala'}}
for key,value in person.items():
    if key=="gender":
        for val in value:  
            a=val
        print(val)


