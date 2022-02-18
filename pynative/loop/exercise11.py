# mijn versie
start = int(input("start number"))
end = int(input("end number"))
print("Prime numbers are: ")
print()

for k in range(start, end, 1):
    prime = True
    for i in range(2, 10, 1):
        if k % i == 0:
            prime = False

    if prime == True:
        print(k)

# site versie
# start = 25
# end = 50
# print("Prime numbers between", start, "and", end, "are:")
#
# for num in range(start, end + 1):
#     # all prime numbers are greater than 1
#     # if number is less than or equal to 1, it is not prime
#     if num > 1:
#         for i in range(2, num):
#             # check for factors
#             if (num % i) == 0:
#                 # not a prime number so break inner loop and
#                 # look for next number
#                 break
#         else:
#             print(num)











