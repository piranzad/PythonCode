def range_five(_from, _to, _step):
    # n1 = 10
    while _from % _step == 0 and _from <= _to+1:
        print(_from)
        _from = _from+_step


fromc = int(input("Please enter from: "))
to = int(input("Please enter to: "))
step = int(input("Please enter range number: "))
range_five(fromc, to, step)
