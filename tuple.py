"""
TUPLES
- store multiple items in a single variable
- defined using () brackets
- it is ordered, unchangeable/immutable but allows duplicate values
- can be of any data type.
There are two variations:
    1. fruits =("Mangoes",14, True, False, "Oranges",1,"Avocados",2,"Mangoes",56,"Pineapple")
    2.fruits =tuple(("Mangoes",14, True, False, "Oranges",1,"Avocados",2,"Mangoes",56,"Pineapple"))
    TUPLE OPERATIONS:
    1. len() - determine the list items/number in a list.
    2. almost all tuple items are accessed in a similar manner to list
"""
fruits = tuple(("Apples", "Mangoes", "Oranges", "Berries"))
print(fruits)
print("The total items in the list are\t", int(len(fruits)))

# Accessing tuple items - similar to list
print(fruits[1])
print(fruits[-2])
print(fruits[1:3])
print(fruits[1:])
print(fruits[:-1])

# Checking if an item is in a tuple
"""
1. declare a variable that will be used to search
2. Create an if statement

searchvar = input("Enter a value to search for /n")
if searchvar in fruits:
    print("Item exists")
else:
    print("Item doesn't exist")
    
How to make a tuple mutable:
1. Convert to a list
2. Change the list
3. Convert the list back to a tuple
"""

mypc = ("Hp", "16GB RAM", "500GB HDD", "200,000")
# convert the tuple to a list using the list() method
mypc = list(mypc)
# change the list - in this case we are adding content to the list
mypc.insert(1, "iCore 7 , Gen 12 , 2.5GHz")
# convert the list back to the tuple
mypc = tuple(mypc)
# print the output
print(mypc)
