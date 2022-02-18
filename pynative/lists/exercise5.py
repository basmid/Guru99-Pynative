
# 10 400
# 20 300
# 30 200
# 40 100

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

#mijn versie
i = 0
j = len(list2) - 1

while i < len(list1):
    print(list1[i],"",list2[j])
    i = i + 1
    j = j - 1

#site versie

for x, y in zip(list1, list2[::-1]):
    print(x, y)