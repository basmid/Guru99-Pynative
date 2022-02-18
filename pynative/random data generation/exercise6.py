#Exercise 6: Generate a random Password which meets the following conditions

# Password length must be 10 characters long
# It must contain at least 2 upper case letters, 1 digit, and 1 special symbol

import string
import random
from string import ascii_lowercase

upp1 = random.choice(string.ascii_uppercase)
upp2 = random.choice(string.ascii_uppercase)
dig =  random.choice(string.digits)
spe_char = random.choice(string.punctuation)
char6 = "".join(random.choice(ascii_lowercase) for i in range(6))
password = upp1 + upp2 + dig + spe_char + char6
print(password)