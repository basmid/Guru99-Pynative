

def merge_list(list1, list2):
    list3 = []
    for i in list1:
        if i % 2 != 0:
            list3.append(i)

    for i in list2:
        if i % 2 == 0:
            list3.append(i)

    return list3

print(merge_list([10, 20, 25, 30, 35, 33],[40, 45, 60, 75, 99, 100]))
