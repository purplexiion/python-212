# defining a list in python
cars = ["Benz", "Passat", "Volvo", "Audi"]
other = ["Rolls Royce", "Bugatti", "Maserati", "Honda"]

# ''' is used for multiline comments
val = input("Enter item to search for\n")
if val in cars:
    print("Item Exists")
else:
    print("")
# printing values in a list
print(cars)
# accessing items in a list using an index
print(cars[0]) # The first one. Lists have indexes beginning from 0
print(cars[1:2]) # second index
print(cars[2]) # third index
print(cars[-1]) # last index; can be defined as -1 or (n-1)

# display the total number of items in a list -done using the len()function
print(len(cars))

# THE FIRST NUMBER REPRESENTS THE INDEX WHILE THE SECOND REFERS TO THE ABSOLUTE POSITION.
# Hence, the item having the first index is picked and the item having the actual number is picked next
print(cars[0:3])

# Displaying the second item in a list
print(cars[1])
# last index via negative indexing
print(cars[-1])
# 1st and 2nd item in a list
print(cars[0:2])
# third and fourth item in a list
print(cars[2:4])
# the second up to the last item
print(cars[1:])

# inserting an item in a list in python(with specifying the index). done using the insert() method.
cars.insert(1, "Ferrari")
print(cars)

# inserting an item at the end of the list. Using append() method.
cars.append("Toyota")
print(cars)

# Appending items from one list to another using the extend() method.
cars.extend(other)
print(cars)

# removing item from a list without specifying the index, remove() method.
cars.remove("Benz")
print(cars)

# removing an item from a list using the pop() method
cars.pop(0)
print(cars)

# deleting an item from the list(the last item) without making use of indexing
cars.pop()
print(cars)

# clearing the list using clear() method
cars.clear()
print(cars)

# clear vs delete: in clear, the list is there, it is just empty. Delete removes the whole content of the list

# using the delete() method - an error will come when you print the list as it has been deleted
'''
NameError: name 'cars' is not defined
'''
del cars
print(cars)

