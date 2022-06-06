# Online status
# The aim of this challenge is, given a dictionary of people's online status, 
# to count the number of people who are online.
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    "Crux":"online",
}
count=0
for i in statuses:
    if statuses[i]=="online":
        count+=1
print(count)
# count=0
# for k,v in statuses.items():
#     if v=="online":
#         count+=1
# print(count)



