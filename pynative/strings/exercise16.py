#mijn versie
#Removal all characters from a string except integers

str1 = 'I am 25 years and 10 months old'

numeric_filter = filter(str.isdigit, str1)
numeric_string = "".join(numeric_filter)

print(numeric_string)

# site versie
str1 = 'I am 25 years and 10 months old'
print("Original string is", str1)

# Retain Numbers in String
# Using list comprehension + join() + isdigit()
res = "".join([item for item in str1 if item.isdigit()])

print(res)
