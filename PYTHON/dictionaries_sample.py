notify = {
    1: "number 1",
    2: "number 2",
    3: "number 0",
}

user = int(input("select an option(0/1/2): "))

if user in notify:
    print(notify[user])
else:
    print("wrong input")