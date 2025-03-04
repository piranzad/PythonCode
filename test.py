# PI = 3.14
# radius = 5
# area = radius * radius * 3.14
# print(area)

# print("*"*2)
# print("*"*3)
# print("*"*4)
#########################################################################
# user_name = input("Name: ")
# family_nam = input("Family Name: ")
# nummber = input("Number Tel: ")
# print("Your Data are: " + user_name + " " + family_nam+" "+nummber)
#########################################################################
# dyta Type
# age = 25  # int
# revnue_rate = 10.2  # Float
# name = "Pouya"  # String
# is_Marrid = False  # Bool
# email = None  # Null
#########################################################################
# a = 10
# b = 5
# res = a + b
# print("res" + res)# \error
# print("res %d and %d is %d" % (a, b, res))
###########################################################################
# oprations
# Artthemetic Oprations

# Olviyat
# result_olvayit = ((n1+(n1**n2)/4) + ((n1/n2) - n2))
# print(result_olvayit)
# ADD(+)
# result_add = n1 + n2
# print("Result %d and %d is %d =" % (n1, n2, result_add))
# n1 += n1
# print("Result %d is =" % (n1))
# sub(-)
# result_sub = n1-n2
# print("result_sub %d and %d is  %d =" % (n1, n2, result_sub))
# n1 -= 4
# print("Result %d is =" % (n1))
# Multi(*)
# result_multi = n1 * n2
# print("result_multi %d and %d is  %d=" % (n1, n2, result_multi))
# n1 *= 4
# print("Result %d is =" % (n1))
# Div(/)
# result_div = n1 / n2
# print("result_div %d and %d is %d =" % (n1, n2, result_div))
# n1 /= 4
# print("Result %d is =" % (n1))
# mod(%)
# result_modol = n1 % n2
# print("result_modol %d and %d is %d =" % (n1, n2, result_modol))
# n1 %= 4
# print("Result %d is =" % (n1))
# expont(**)
# result_expont = n1 ** n2
# print("result_expont %d and %d is  %d=" % (n1, n2, result_expont))
# n1 **= 4
# print("Result %d is =" % (n1))
# floor(//)
# result_expont = n1 // n2
# print("result_expont %d and %d is %d =" % (n1, n2, result_expont))
# n1 //= 4
# print("Result %d is =" % (n1))


try:
    n1 = int(input("please Enter Nummber1"))
    n2 = int(input("please Enter Nummber2"))
except:
    print("eshtebah zadi dadash")
else:
    if n1 >= n2 and n1 < 100:
        res1 = n1*n2
        print(res1)
    elif n1 >= n2 or n1 < 100:
        res2 = n1+1
        print(res2)
finally:
    print("pouyaaaaaaaaaaaaaaa")
