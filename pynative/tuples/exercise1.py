#mijn versie
tuple1 = (10, 20, 30, 40, 50)

#(50, 40, 30, 20, 10)

new_tup = ()
for k in reversed(tuple1):
    new_tup = new_tup + (k,)

print(new_tup)

#site versie
# tuple1 = (10, 20, 30, 40, 50)
# tuple1 = tuple1[::-1]
# print(tuple1)

