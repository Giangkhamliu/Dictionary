# Write a program to print 'exists' if entered key already exists in the
#  dictionary and print 'not exists' if the entered key does not exist.

dict1={"name":"Raju", "marks":56}
def key(x):
    if x in dict1:
        print("Exist",dict1[x])
    else:
        print("NOt Exist")
x=input("Enter the key:-")
key(x)
