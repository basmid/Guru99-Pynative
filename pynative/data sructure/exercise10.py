#mijn versie
#Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number

# tuple (87, 45, 41, 65, 99)
# min: 41
# max: 99
#sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
sample_list = [87, 52, 44, 53, 54, 87, 52, 53]
# unique items [87, 45, 41, 65, 99]

for num in sample_list:
    if sample_list.count(num) > 1:
        sample_list.remove(num)

print(sample_list)

num_in_tuples = ()
num_in_tuples = sample_list.copy()
print(num_in_tuples)

print(max(num_in_tuples))
print(min(num_in_tuples))

#site versie
# sample_list = [87, 52, 44, 53, 54, 87, 52, 53]
#
# print("Original list", sample_list)
#
# sample_list = list(set(sample_list))
# print("unique list", sample_list)
#
# t = tuple(sample_list)
# print("tuple ", t)
#
# print("Minimum number is: ", min(t))
# print("Maximum number is: ", max(t))