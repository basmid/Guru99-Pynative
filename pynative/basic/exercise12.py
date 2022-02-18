

income = int(input("enter the amount"))

tax = 0
if(income <= 10000):
    tax = 0
elif(income <= 20000):
    tax = (income - 10000) * 0.1
elif(income > 20000):
    tax = 1000 + ((income - 20000) * 0.2)

print(tax)

