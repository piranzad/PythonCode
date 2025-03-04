def time_date(tag, monat, jahr):
    res = "print Tag %d, Monat %d, Jahr %d" % (tag, monat, jahr)
    return res


t = int(input("Bitte sagen Sie den Tag: "))
m = int(input("Bitte sagen Sie den Monat: "))
j = int(input("Bitte sagen Sie das Jahr: "))
print(time_date(t, m, j))
