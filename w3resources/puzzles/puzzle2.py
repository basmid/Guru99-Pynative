
list = [19, 19, 4, 4, 5, 5, 5,2]

def test(list):

    fifth = list[4]
    total = 0
    for i in list:
        if i == fifth:
            total = total + 1

    return len(list) == 8 and total == 3

print(test(list))








