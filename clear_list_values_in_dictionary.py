def check(dictionary):
    for i in dictionary:
        dictionary[i].clear()
    return dictionary
dictionary = { 
               'C1' : [10,20,30], 
               'C2' : [20,30,40],
               'C3' : [12,34]}
print(check(dictionary)) 
