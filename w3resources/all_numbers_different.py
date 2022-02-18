
from collections import Counter

sequence = 7659
str_numbers = str(sequence)

all_diff = True
x = range(10)
for n in x:
    if str_numbers.count(str(n)) > 1:
        print("not all different")
        all_diff = False

print(all_diff)





