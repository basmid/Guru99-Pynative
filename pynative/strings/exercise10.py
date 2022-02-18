
# str1 = "Apple"
# # Expected Outcome:
# #
# # {'A': 1, 'p': 2, 'l': 1, 'e': 1}
#
# aCount = str1.count('a')
# pCount = str1.count('p')
# lCount = str1.count('l')
# eCount = str1.count('e')
#
# dict = {'A': aCount, 'p': pCount, 'l': lCount, 'e': eCount}
# print(dict)

str1 = "Apple"
# create a result dictionary
char_dict = dict()

for char in str1:
    count = str1.count(char)
    # add / update the count of a character
    char_dict[char] = count
print('Result:', char_dict)