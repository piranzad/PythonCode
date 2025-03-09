def print_books(list_of_book):
    for each_book in list_of_book:
        print(each_book)


my_list2 = ["pouya", "negin"]
my_list = list(input("NAme ketab ro vard kon"))
print_books(my_list2)
print_books(my_list)
######################################


def get_nummber():
    list_of_nummber = []
    for each_nummber in range(1, 10):
        list_of_nummber.append(each_nummber)
    return list_of_nummber


number = get_nummber()
print(number)


def get_nummber_set():
    list_of_nummber_set = {}
    for each_nummber_set in range(1, 10):
        list_of_nummber.append(each_nummber_set)
    return list_of_nummber_set


number_set = get_nummber()
print(number_set)
