
str = "klaas piet jan klaas piet piet piet piet klaas"

list = list(str.split(" "))

duplicate_dict={} # a dictionary to store each of them.
for i in list:#loop through them.
    duplicate_dict[i]=list.count(i)
print(duplicate_dict)#to get the occurence of each of the element









