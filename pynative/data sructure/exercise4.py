
#mijn versie
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
dict_count = {}
##Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}

for x in sample_list:
    if x not in dict_count:
        dict_count[x] = sample_list.count(x)

print(dict_count)

#site versie
# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
# print("Original list ", sample_list)
#
# count_dict = dict()
# for item in sample_list:
#     if item in count_dict:
#         count_dict[item] += 1
#     else:
#         count_dict[item] = 1
#
# print("Printing count of each item  ", count_dict)


