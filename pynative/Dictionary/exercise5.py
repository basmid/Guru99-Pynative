#mijn versie
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

#{'name': 'Kelly', 'salary': 8000}

new_dict = {}
i = 0
while i < len(keys):
    new_dict[keys[i]] = sample_dict.get(keys[i])
    i = i + 1

print(new_dict)

# site versie
# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york" }
#
# keys = ["name", "salary"]
#
# newDict = {k: sampleDict[k] for k in keys}
# print(newDict)
