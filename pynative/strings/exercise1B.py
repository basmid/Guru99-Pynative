# mijn versie, geen functie
str1 = "JhonDipPeta"
#Dip

str_len = len(str1)
print(str_len)
middle = int(str_len / 2)
print(middle)
first_char = middle - 1
last_char = middle + 2

new_str1 = str1[int(first_char):int(last_char)]
print(new_str1)


# site versie
# def get_middle_three_chars(str1):
#     print("Original String is", str1)
#
#     # first get middle index number
#     mi = int(len(str1) / 2)
#     print(mi)
#
#     # use string slicing to get result characters
#     res = str1[mi - 1:mi + 2]
#     print("Middle three chars are:", res)
#
# get_middle_three_chars("JhonDipPeta")
# #get_middle_three_chars("JaSonAy")