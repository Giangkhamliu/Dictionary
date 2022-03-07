def test(dictt):
    min_value=1
    result = [key for key, value in dictt.items() if len(value) == (min_value)] 
    return result    
dictt = {
 'V': [10, 12],
 'VI': [10],
 'VII': [10, 20, 30, 40],
 'VIII': [20],
 'IX': [10,30,50,70],
 'X': [80]
 }
print("The shortest value:-")
print(test(dictt))



