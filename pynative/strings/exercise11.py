

str1 = "PYnative"
str2 = ""

length = len(str1) - 1
while length >= 0:
    print(str1[length])
    str2 = str2 + str1[length]
    length = length - 1

print(str2)

#evitanYP