
num1 = 17
num2 = int(input("please enter a number"))

def distance(x, y):
    if x >= y:
        result = x - y
    else:
        result = y - x
    return result

print(distance(num1,num2))


