def test(dictt):
    result = {}
    for val in dictt.values(): 
        result[val] = len(val) 
    return result    
color_dict = {'1' : 'Austin Little', '2' : 'Natasha Howard', '3' : 'Alfred Mullins'}
print(test(color_dict))