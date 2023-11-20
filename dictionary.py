# Dictionary
# stores values in key:value pairs for example:
products = {"Name": "Fridge", "Code:": "P2345", "Price": 30000, "Quantity": 5, "Expiry date": "31-10-2023"}

# access the dictionary key - output is the value of the given key
print(products)

# using the key name to access the value
print(products["Price"])

# using the get method
print(products.get("Code"))

# using the keys()
print(products.keys())

# using the values()
print(products.values())

# getting both the keys and values
print(products.items())

# to add a new item to the dictionary
products["Re-order Level"] = 3
print(products)

# it can also be used to update/ change values in an existing key
products["Price"] = 120000.000
print(products)

# updating using the update({key: new value}) method
products.update({"Quantity": 9})
print(products)

# removing an item using the pop() method
products.pop("Price")
print(products)

# removing using the del property
del products["Quantity"]
print(products)

# to remove the last item
products.popitem()
print(products)
