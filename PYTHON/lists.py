#append a new element to the target list
#extends allows to add one list to another
#insert add a new list element right before a special list
#del which deletes 
x = [1,2,3]
x.append("lee")
print(x)

y = [7,8]
x.append(y)
print(x)

x.extend(y)
print(x)

x.insert(2, "maru")
print(x)

del x[2] #deleting value at index 2

del x[2:] #deletes elements with index greater than or equal to 2
x.remove(7) # it removes the first instance of 7

list.pop(5) #removes the item at the given position
list.sort() # sorts a list (they must be of the same type)
list.reverse() # reverses the order of the elements in the list