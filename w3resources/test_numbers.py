


def test_numbers(num1,num2):
    meet_criteria = False
    if num1 == num2:
        meet_criteria = True
    elif num1 + num2 == 5:
        meet_criteria = True
    elif abs(num1 - num2) == 5:
        meet_criteria = True
    print(meet_criteria)

test_numbers(2,9)




