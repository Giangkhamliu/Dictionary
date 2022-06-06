dict1 = {1: ["John", 21, 'CS'],
         2: ["Tim", 20, 'EE'],
         3: ["Steve", 21, 'Civil'],
         }
print("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COURSE'))
for key, value in dict1.items():
    name, age, course = value
    print("{:<10} {:<10} {:<10}".format(name, age, course))

