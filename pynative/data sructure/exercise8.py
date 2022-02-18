#site versie
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

print("List:", roll_number)
print("Dictionary:", sample_dict)

# create new list
roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
print("after removing unwanted elements from list:", roll_number)

#site versie, niet werkend
# # Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary.
# # If not, delete it from the list
#
# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
#
# #After removing unwanted elements from list [47, 69, 76, 97]
#
# for x in roll_number:
#     #print(x)
#     indict = False
#     for item in sample_dict.values():
#         #print(x)
#         #print(item)
#         if x == item:
#             indict = True
#
#     if indict == False:
#         roll_number.remove(x)
#
# print(roll_number)