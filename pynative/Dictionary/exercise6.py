# mijn versie
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]
#{'city': 'New york', 'age': 25}

for x in keys:
    if x in sample_dict: del sample_dict[x]

print(sample_dict)

#site versie
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# # Keys to remove
# keys = ["name", "salary"]
#
# for k in keys:
#     sample_dict.pop(k)
# print(sample_dict)