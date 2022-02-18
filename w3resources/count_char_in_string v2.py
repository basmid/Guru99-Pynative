
#test_str = "abdeeeeaaaaadc"

file = open("str_count_char_in_string.txt", "r")
test_str = file.read()
file.close()
#print(test_str)

all_freq = {}

for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

print("Count of all characters in str is :\n " + str(all_freq))