#mijn versie
# Chunk  1 [11, 45, 8]
# After reversing it  [8, 45, 11]
# Chunk  2 [23, 14, 12]
# After reversing it  [12, 14, 23]
# Chunk  3 [78, 45, 89]
# After reversing it  [89, 45, 78]


sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

list1 = sample_list[0:3]
list1.reverse()
print(list1)
list2 = sample_list[3:6]
list2.reverse()
print(list2)
list3 = sample_list[6:9]
list3.reverse()
print(list3)

#site versie
# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# print("Original list ", sample_list)
#
# length = len(sample_list)
# chunk_size = int(length / 3)
# start = 0
# end = chunk_size
#
# # run loop 3 times
# for i in range(3):
#     # get indexes
#     indexes = slice(start, end)
#
#     # get chunk
#     list_chunk = sample_list[indexes]
#     print("Chunk ", i, list_chunk)
#
#     # reverse chunk
#     print("After reversing it ", list(reversed(list_chunk)))
#
#     start = end
#     end += chunk_size