#mijn versie
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
list = []
#[47, 52, 44, 53, 54]

for x in speed:
  if speed[x] not in list:
     list.append(speed[x])

print(list)

#site versie
# speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53,
#          'july': 54, 'Aug': 44, 'Sept': 54}
#
# print("Dictionary's values - ", speed.values())
#
# speed_list = list()
#
# # iterate dict values
# for val in speed.values():
#     # check if value not present in a list
#     if val not in speed_list:
#         speed_list.append(val)
# print("unique list", speed_list)

