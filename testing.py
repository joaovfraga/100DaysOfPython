def highest_number(list1):
    highest = 0
    for num in range(len(list1)):
        if list1[num] > highest:
            highest = list1[num]

    print(highest)


my_list = [1, 300, 5000, 50, 1000, 8, 9000]
highest_number(my_list)
