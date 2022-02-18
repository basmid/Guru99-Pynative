#mijn versie
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
i = 0
while i < len(my_list):
    if i % 2 != 0:
        print(i)
        print(my_list[i])

    i = i + 1


#versie site
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# # stat from index 1 with step 2( means 1, 3, 5, an so on)
# for i in my_list[1::2]:
#     print(i, end=" ")