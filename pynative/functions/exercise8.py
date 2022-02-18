
#mijn versie
def create_list():
    x = range(4, 30, 2)
    list = []
    for n in x:
        list.append(n)

    return list

list1 = create_list()
print(list1)

#site versie
#print(list(range(4, 30, 2)))