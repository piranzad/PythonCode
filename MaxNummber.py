def max_nummber(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        result = n1
        return result
    elif n2 > n1 and n2 > n3:
        result = n2
        return result
    else:
        result = n3
    print("in %d in %d in %d mishe in %d" % (n1, n2, n3, result))


nm1 = int(input("Bitte sagen Sie den Nummer 1: "))
nm2 = int(input("Bitte sagen Sie den Nummer: "))
nm3 = int(input("Bitte sagen Sie das Nummer: "))
max_nummber(nm1, nm2, nm3)
