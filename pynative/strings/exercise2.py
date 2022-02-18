#mijn versie
s1 = "Ault"
s2 = "Kelly"
#AuKellylt

s1_len = len(s1)
print(s1_len)
middle = int(s1_len / 2)
print(middle)

s1 = s1[:middle] + s2 + s1[middle:]
print(s1)

#versie site
# def append_middle(s1, s2):
#     print("Original Strings are", s1, s2)
#
#     # middle index number of s1
#     mi = int(len(s1) / 2)
#
#     # get character from 0 to the middle index number from s1
#     x = s1[:mi:]
#     # concatenate s2 to it
#     x = x + s2
#     # append remaining character from s1
#     x = x + s1[mi:]
#     print("After appending new string in middle:", x)
#
# append_middle("Ault", "Kelly")



