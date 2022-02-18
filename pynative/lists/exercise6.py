
#mijn versie
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# ["Mike", "Emma", "Kelly", "Brad"]

for ele in list1:
    if ele == "":
        list1.remove(ele)

print(list1)

# site versie
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
#
# # remove None from list1 and convert result into list
# res = list(filter(None, list1))
# print(res)