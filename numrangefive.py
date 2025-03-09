def range_five(n1, n2):
    # for each_number in range(n1, n2,5):
    # print(each_number)

    for each_number in range(n1, n2+1):
        if each_number % 5 == 0:
            print(each_number)


get_number_1 = int(input("Please enter your first number: "))
get_number_2 = int(input("Please enter your second number: "))
range_five(get_number_1, get_number_2)
