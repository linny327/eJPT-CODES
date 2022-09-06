# a function is a group of statements that gets executed when function is called
#synax
#from ast import Expression


#def function_name(parameter1, parameter2, ...):
#    function_statements
#   return Expression

#def indicates the funx definition
#function_name is the identifier of the function
#parameters is a comma-separated list of variables
#function_statements is the body of the function
#return exits a function and gives the execution back to the caller

from re import X


def my_sum (x,y):
    """return the addition"""
    return x + y

c = my_sum(7,8)
#print(c)
print("sum is: ", c)
print(my_sum(1,2))
print("my_sum doc:", my_sum.__doc__)


#global variables
def change_global ():
    """return variable"""
    global x
    x = 1
x = 4
print("x before calling the function:", x) #4
change_global()
print("x after calling the function:", x)#1