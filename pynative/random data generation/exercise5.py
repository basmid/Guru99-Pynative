#mijn versie
#Generate random String of length 5

#Note: String must be the combination of the UPPER case and lower case letters only.
# No numbers and a special symbol.

import string
import random

res = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5))

# print result
print("The generated random string : " + str(res))

#site versie
# import random
# import string
#
# def randomString(stringLength):
#     """Generate a random string of 5 charcters"""
#     letters = string.ascii_letters
#     return ''.join(random.choice(letters) for i in range(stringLength))
#
# print ("Random String is ", randomString(5) )