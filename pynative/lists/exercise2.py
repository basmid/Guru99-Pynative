#mijn versie
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

#['My', 'name', 'is', 'Kelly']
list3 = []
i = 0
while i < len(list1):
    word = list1[i] + list2[i]
    list3.append(word)
    i = i + 1

print(list3)

#site versie
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)