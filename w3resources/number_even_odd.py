
#my version
num = (int(input("please enter a number")))

num_2 = num / 2
print(num_2)
last_num = int(str(num_2).split('.')[1][0])
print(last_num)

if last_num == 0:
    print("number is even")
elif last_num == 5:
    print("number is odd")

#w3resource version
# num = int(input("Enter a number: "))
# mod = num % 2
# if mod > 0:
#     print("This is an odd number.")
# else:
#     print("This is an even number.")







