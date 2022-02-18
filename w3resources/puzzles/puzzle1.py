
#list = [19, 19, 15, 5, 3, 5, 5, 5, 1]
#
# elm19_2 = 19
# elm5_3 = 5
#
# el19 = list.count(elm19_2)
# el5 = list.count(elm5_3)
#
# if el19 == 2 and el5 >= 3:
#     print("True")
# else:
#     print("False")

list = [19, 19, 15, 4, 3, 2, 5, 5, 1]

def test(list):
    return list.count(19) == 2 and list.count(5) >= 3

print(test(list))