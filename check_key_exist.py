# Write a Python script to check whether a given key already exists in a dictionary. 
dic={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121,"name":"Grace","age":23}
keys=int(input("Enter the keys:-"))
if keys in dic.keys():
        print("Yes",keys, "exist")
else:
        print("no",keys,"exist")