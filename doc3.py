# A Python Dictionary contains List as value. Write a Python program to clear the list values in
# the said dictionary.
d={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
for i,j in d.items():
    j.clear()
print(d)

# output: {'C1': [], 'C2': [], 'C3': []}