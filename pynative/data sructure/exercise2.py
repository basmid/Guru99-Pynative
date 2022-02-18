
#mijn versie
list1 = [34, 54, 67, 89, 11, 43, 94]

num = list1[4]

list1.remove(num)
# List After removing element at index 4  [34, 54, 67, 89, 43, 94]
print(list1)
list1.insert(2, num)
# List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
print(list1)
list1.insert(len(list1), num)
# List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]
print(list1)

# site versie
# sample_list = [34, 54, 67, 89, 11, 43, 94]
#
# print("Original list ", sample_list)
# element = sample_list.pop(4)
# print("List After removing element at index 4 ", sample_list)
#
# sample_list.insert(2, element)
# print("List after Adding element at index 2 ", sample_list)
#
# sample_list.append(element)
# print("List after Adding element at last ", sample_list)