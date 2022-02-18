
# str1 = "/*Jon is @developer & musician"
# #"Jon is developer musician"
#
# # initializing punctuations string
# punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#
# for ele in str1:
#     if ele in punc:
#         str1 = str1.replace(ele, "")
#
# # printing result
# print("The string after punctuation filter : " + str1)

import string

str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)

new_str = str1.translate(str.maketrans('', '', string.punctuation))
print("New string is ", new_str)





