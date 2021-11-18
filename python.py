import sys as sy
## from sys import *
from fonction import *
from sys import argv
print("Success")

fruit = "banana"
quantity = 3
pie_crust = "empty"
isOvenOn = False

print(f"You  have {quantity} {fruit} and the pie  crust  is {pie_crust} , is the  oven on? {isOvenOn}")

pie_crust = "empty"# Start of your  code (3 lines)
fruit = "apple"
quantity = 5
isOvenOn = False
# End of your  code
print(f"You  have {quantity} {fruit}",
f" and the pie  crust  is {pie_crust},",
f" is the  oven on? {isOvenOn}")

def  print_hello_please () :
    print("Hello")
print_hello_please ()

def  print_hello_with_my_name_please(myName):
    print("Hello", myName)
print_hello_with_my_name_please("Jacqueline")
my_current_age = 0

def  calc_my_age_in_two_years(myCurrentAge):
    print(f"You are {my_current_age} years  old")
    my_age_in_two_years = myCurrentAge + 2
    return  my_age_in_two_years
my_age_in_two_years = calc_my_age_in_two_years(33)
print(f"In two years , i'll be {my_age_in_two_years} years  old")

def prepMyFruit(nb, fruit, pir_crust):
    print(f"you put {nb} {fruit} on the crust")
    pir_crust = f"filled with delicious {fruit}"
    return (pir_crust)
print("my pie is", prepMyFruit(3, "apple", "empty"))


def turn_on_oven(oven):
    return (True)
print("the oven is", turn_on_oven(False))

def ask_me_about_string(string):
    if(string[0] == 'a'):
        print("That's an A")
    if (len(string) < 5):
        print("error, need longer string")
    if (string[0].upper() == string[len(string) - 1].upper()):
        print("hey are the same O_O")
    else:
        print("what a boring string...")

ask_me_about_string("kayaK")

def  get_sys_argc ():
    return  len(sy.argv)
print(get_sys_argc ())

def  get_sys_argc():
    try:
        print("Success", file=stdout)
    except:
        print("You  must  import  all the sys  module")
    return len(argv)
print(get_sys_argc())

def  get_sys_argc3():
    try:
        print("You  must  only  import  the  argv  methode", file=stdout)
    except:
        print("Success")
    return  len(argv)
get_sys_argc3()

fib(5)

print1_to_10()


resto_a_proximite = ["bk", "otacos", "cazada", "jules"]
print("ils  font  des  pizzas a la", resto_a_proximite [2])

print("ils  font  des  carry  chez", resto_a_proximite [-1])