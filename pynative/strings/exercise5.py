
def check_string():

    str = "P@#yn26at^&i5ve"
    #str = "3hd78!!!@HHa78"
    chars = 0
    digits = 0
    symbols = 0

    for element in str:
        if element.isalpha():
            chars = chars + 1
        elif element.isdigit():
            digits = digits + 1
        else:
            symbols = symbols + 1

    return chars, digits, symbols

result = check_string()
print("Chars: ",result[0], end="\n")
print("Digits: ",result[1], end="\n")
print("Symbols: ",result[2])



