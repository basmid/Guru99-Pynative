
def multiplication_or_sum(num1,num2):
    multiplication = num1 * num2
    sum = num1 + num2

    if multiplication > 1000:
        return multiplication
    else:
        return sum

print("The result is: ", multiplication_or_sum(15,100))





