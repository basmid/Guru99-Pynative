
#You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200.
#Only update the first occurrence of an item.

#mijn versie
list1 = [5, 10, 15, 20, 25, 50, 20]

#[5, 10, 15, 200, 25, 50, 20]

for i in range(len(list1)):
    if list1[i] == 20:
        list1[i] = 200
        break

print(list1)

#site versie
# list1 = [5, 10, 15, 20, 25, 50, 20]
#
# # get the first occurrence index
# index = list1.index(20)
#
# # update item present at location
# list1[index] = 200
# print(list1)