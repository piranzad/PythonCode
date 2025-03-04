# function definition
def validate_free_shipping(total_cost):
    if total_cost > 40:
        print("The order is eligible for free shipping!")
    else:
        print("The order is not eligible for free shipping!")


# function call
total_cost = int(input("Please Enter Total Cost Of Items: "))
validate_free_shipping(total_cost)
