# mijn versie
num = 2
num_str = str(num)
num2_str = ""
tot = 0
sequence = 5
i = 1
while i <= sequence:
    num2_str = num2_str + num_str
    print("i ",i)
    print("num2", num2_str)
    num_str2 = num_str
    i = i + 1
    tot = tot + int(num2_str)

print(tot)
#2 + 22 + 222 + 2222 + 22222 = 24690

# site versie
# n = 5
# # first number of sequence
# start = 2
# sum_seq = 0
#
# # run loop n times
# for i in range(0, n):
#     print(start, end="+")
#     sum_seq += start
#     # calculate the next term
#     start = start * 10 + 2
# print("\nSum of above series is:", sum_seq)







