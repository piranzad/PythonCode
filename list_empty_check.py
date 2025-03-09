# function definition
def is_list_empty(my_list):
    if len(my_list) == 0:
        return True
    else:
        return False


# function call
my_list = []
print(is_list_empty(my_list))
