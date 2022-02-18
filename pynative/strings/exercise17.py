# mijn versie
#Find words with both alphabets and numbers

str1 = "Emma25 is Data scientist50 and AI Expert"

#Emma25
#scientist50

for word in str1.split():
    if any(c.isalpha() for c in word) and any(c.isdigit() for c in word):
        print(word)

# site versie
# str1 = "Emma25 is Data scientist50 and AI Expert"
# print("The original string is : " + str1)
#
# res = []
# # split string on whitespace
# temp = str1.split()
#
# # Words with both alphabets and numbers
# # isdigit() for numbers + isalpha() for alphabets
# # use any() to check each character
#
# for item in temp:
#     if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
#         res.append(item)
#
# print("Displaying words with alphabets and numbers")
# for i in res:
#     print(i)