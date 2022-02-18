# mijn versie
def lowupp():

    str = "aHHerLkk"
    low = ""
    upp = ""
    newstr = ""

    for element in str:
        if element.islower():
            low = low + element
        else:
            upp = upp + element

    newstr = low + upp
    return newstr

str1 = lowupp()
print(str1)

#site versie
# str1 = "PYnAtivE"
# print('Original String:', str1)
# lower = []
# upper = []
# for char in str1:
#     if char.islower():
#         # add lowercase characters to lower list
#         lower.append(char)
#     else:
#         # add uppercase characters to lower list
#         upper.append(char)
#
# # Join both list
# sorted_str = ''.join(lower + upper)
# print('Result:', sorted_str)



#yaivePNT