
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
#
# #['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
#
# i = 0
# j = 0
# print(len(list1))
# while j < len(list1):
#     print(list1[i] + list2[j])
#     j = j + 1
# i = i + j

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

res = [x + y for x in list1 for y in list2]
print(res)




