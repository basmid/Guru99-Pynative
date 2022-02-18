
#Write a Python program to remove items 10, 20, 30 from the following set at once.
set1 = {10, 20, 30, 40, 50}

#{40, 50}

to_delete = [10,20,30]

set1.difference_update(to_delete)
print(set1)