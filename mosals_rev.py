def moslas(number):
    i = number  # مقداردهی صحیح
    while i <= number:
        print("*" * i)  # چاپ ستاره‌ها بر اساس مقدار i
        i -= 1  # افزایش مقدار i


get_number = int(input("Please enter your number: "))
moslas(get_number)
