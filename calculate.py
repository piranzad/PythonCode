def calculate_mashin(n1, m, n2):
    if m == "+":
        res = n1+n2
    elif m == "-":
        res = n1-n2
    elif m == "*":
        res = n1*n2
    elif m == "/":
        res = n1/n2
    else:
        return "Invalid opration"
    return (res)


try:
    nummber1 = int(input("Please Enter Nummber 1: "))
    ass = input("Please Enter Assigment 1: ")
    nummber2 = int(input("Please Enter Nummber 2: "))
    print("Result:", calculate_mashin(nummber1, ass, nummber2))
except:
    print("Khar")
else:
    calculate_mashin(nummber1, ass, nummber2)
