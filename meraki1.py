from collections import Counter
dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dic=Counter(dic1)+Counter(dic2)+Counter(dic3)
print(dic)


