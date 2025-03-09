def range_five(n1, n2):
    n1 = 10
    while n1 % 5 == 0 and n1 <= n2+1:
        print(n1)
        n1 = n1+5


get_number_1 = int(input("Please enter your first number: "))
get_number_2 = int(input("Please enter your second number: "))
range_five(get_number_1, get_number_2)
