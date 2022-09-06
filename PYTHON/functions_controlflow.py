#function defination
def a(x):
    print("sum of ", x , "+", x)
    return x + x
def b(x):
    print("Mul of ",x, "*",x)
    return x * x
#assign function a and b to dictionary values and use the key to select them
function_switch = {
    1:a,
    2:b,
}
#print selection menu
user = int(input(""" select an option:   
1) sum
2) mul
"""))
#checking if user is valid if valid get value of user then call right funx using dictionary(function_switch) and print result1
if user in function_switch:
    x = int(input("insert a number: "))
    result = function_switch[user] (x)
    print("result is: ", result)
else:
    print("wrong input")