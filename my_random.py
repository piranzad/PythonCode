import random
side = int(input("Please enter your nummber:  "))
ran_num = random.randint(1, side)
print(ran_num)


my_list = []
for _ in range(11):
    my_list.append(random.randint(0, 100))
print(my_list)
