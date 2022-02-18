# mijn versie
# #Replace each special symbol with # in the following string
import string
str1 = '/*Jon is @developer & musician!!'
str2 = ""
# ##Jon is #developer # musician##
spe_sym = string.punctuation
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(spe_sym)

for x in str1:
    ##print(x)
    if (spe_sym.find(x) != -1):
        str2 = str2 + "#"
    else:
        str2 = str2 + x

print(str2)

# site versie
# import string
#
# str1 = '/*Jon is @developer & musician!!'
# print("The original string is : ", str1)
#
# # Replace punctuations with #
# replace_char = '#'
#
# # string.punctuation to get the list of all special symbols
# for char in string.punctuation:
#     str1 = str1.replace(char, replace_char)
#
# print("The strings after replacement : ", str1)
