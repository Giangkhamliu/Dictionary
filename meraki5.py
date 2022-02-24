# Create a dictionary from 2 lists, where the elements of 1st list
# are the keys and the elements of the 2nd list are the corresponding values.
# output-{“one”:1,”two”:2,”three”:3,”four”:4,”five”:5}

list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
data=dict(zip(list1,list2))
print(data)