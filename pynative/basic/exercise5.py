#mijn versie
def compare_nums(numbers):

    lenght = len(numbers)
    counter = 0
    first_num = numbers[counter]
    while counter < lenght:
        if counter == lenght -1:
            last_num = numbers[counter]
        counter = counter + 1

    print(first_num)
    print(last_num)

    if first_num == last_num:
        return True
    else:
        return False

print(compare_nums([80, 20, 30, 40, 10, 60, 80,60,80]))

#site versie
# def first_last_same(numberList):
#     print("Given list:", numberList)
#
#     first_num = numberList[0]
#     last_num = numberList[-1]
#
#     if first_num == last_num:
#         return True
#     else:
#         return False
#
#
# numbers_x = [10, 20, 30, 40, 10]
# print("result is", first_last_same(numbers_x))
#
# numbers_y = [75, 65, 35, 75, 30]
# print("result is", first_last_same(numbers_y))