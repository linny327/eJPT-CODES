# are mapping objects key:value

c = { "first":"one", "second": 2}
print(c["first"])

len(c)
c["second"] += 1 #add 1 to the value assigned to key "second"
print(c)

c["newkey"]  = "new" #if it doesnt exist it will be added at the start of the dictionary
print(c)

#dictionary.values() returns all the values stored in the dictionary
#dictionary.keys() returns all keys stored in the dictionary
#dictionary.items returns all keys and values

print("second" in c) # if the key exists, returns the associated value

print(c.get("third", "not found" ))