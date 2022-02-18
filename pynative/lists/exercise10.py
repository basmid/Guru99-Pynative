#mijn versie
list1 = [5, 20, 15, 20, 25, 50, 20]

# [5, 15, 25, 50]

iterator = filter(lambda x: (x!=20), list1)
list2 = list(iterator)
print(list2)

#site versie
# list1 = [5, 20, 15, 20, 25, 50, 20]
#
# # list comprehension
# # remove specific items and return a new list
# def remove_value(sample_list, val):
#     return [i for i in sample_list if i != val]
#
# res = remove_value(list1, 20)
# print(res)