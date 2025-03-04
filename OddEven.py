def nummber_odd_even(nummer):
    result = nummer % 2

    if result == 0:
        print(" is %d ODD" % (nummer))
    else:
        print(" is %d Even" % (nummer))


n = int(input("Enter nummer: "))
nummber_odd_even(n)
