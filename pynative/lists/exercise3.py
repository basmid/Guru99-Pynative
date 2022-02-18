
# mijn versie
#Given a list of numbers. write a program to turn every item of a list into its square.
numbers = [1, 2, 3, 4, 5, 6, 7]

#[1, 4, 9, 16, 25, 36, 49]

i = 0
square = []
while i < len(numbers):
    num = numbers[i]
    num2 = num * num
    square.append(num2)
    i = i + 1

print(square)

# site versie
# numbers = [1, 2, 3, 4, 5, 6, 7]
# # result list
# res = []
# for i in numbers:
#     # calculate square and add to the result list
#     res.append(i * i)
# print(res)