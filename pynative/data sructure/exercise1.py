
# mijn versie
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3 = []
for x in l1:
    if (l1.index(x) % 2) != 0:
        l3.append(x)

for y in l2:
    if (l2.index(y) % 2) == 0:
        l3.append(y)

print(l3)

#site versie
# list1 = [3, 6, 9, 12, 15, 18, 21]
# list2 = [4, 8, 12, 16, 20, 24, 28]
# res = list()
#
# odd_elements = list1[1::2]
# print("Element at odd-index positions from list one")
# print(odd_elements)
#
# even_elements = list2[0::2]
# print("Element at even-index positions from list two")
# print(even_elements)
#
# print("Printing Final third list")
# res.extend(odd_elements)
# res.extend(even_elements)
# print(res)