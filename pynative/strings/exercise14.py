# mijn versie
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
new_str_list = []
i = 0
len_str_list = len(str_list)
print(len_str_list)
while i < len_str_list:
    if str_list[i]:
        new_str_list.append(str_list[i])

    i = i + 1

print(new_str_list)

#site versie
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# res_list = []
# for s in str_list:
#     # check for non empty string
#     if s:
#         res_list.append(s)
# print(res_list)