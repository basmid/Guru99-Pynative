

numbers = 2222
str_numbers = str(numbers)
print("lengh: ", len(str_numbers))
len = len(str_numbers)
equal = False
counter = 0
while counter < len -1:
    if str_numbers[counter] == str_numbers[counter + 1]:
        equal = True
        counter += 1
        print(counter)
    else:
        equal = False
        break

print(equal)