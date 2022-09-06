from enum import Flag


grade = int(input("grade number:"))

if grade >= 10:
    print("value is great than 10")
    Flag = True

else:
    print("value is less than 10")
    Flag = False
print(Flag)


#for loop
x = 5
y = 10
for x in range(y):
    print("x:", x)


#CALCULATING THE EXPONENTIAL VALUE
x = int(input("enter a number: "))
for i in range(0,x,2):
    print(i, "^2 = ", i**2)