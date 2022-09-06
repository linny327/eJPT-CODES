# \n means next line
# \t indicates a tab
print(" choose an option: \n\t1) sum\n\t2) sub\n\t0) exit")
u_value = input("Enter option: ")
if u_value == "0":
    print("BYE")
elif u_value == "1":
    print("sum")
elif u_value == "2":
    print("minus")
else:
    print("wrong option")

# there is no switch case in python