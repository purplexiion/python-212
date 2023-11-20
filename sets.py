"""
SETS
- Unordered, unchangable and unindexed
- duplicate values are always ignored
- they are defined with curly brackets
There are two ways of creating a set in Python:
        1. wishlist ={"Python","Java","C++","JavaScript"}
        2. wishlist= set({"Python","Java","C++","JavaScript"}
    Note: a set does not have index(es)
    To access items in a set, we use a for loop

    Qn. Using a for loop, display all the items in the wishlist set
    wishlist = {"Chocolate", "Ice Cream", "Pizza", 'Ford Mustang GT500 in the color purple'}
    for i in wishlist:
    print(i)
    print("\n")

    # using the add method
    wishlist.add("shoes")
    print(wishlist)

    # remove() and discard() method
    wishlist.remove("Chocolate")
    print(wishlist)

    # if one is removing an item that does not exist in the list, an error is brought using the remove() method
    wishlist.discard("Chocolate")
    print(wishlist)

    # random question. Why does this happen??
    mywishlist = set("pizza")
    print(mywishlist)

    delete the last item in a list
    x = wishlist.pop()
    print(x)
    print(wishlist)

    deleting a whole dictionary
    wishlist = {"Chocolate", "Ice Cream", "Pizza", 'Ford Mustang GT500 in the color purple'}
    del wishlist
    print(wishlist)

"""                         
# random question. Why does this happen??
mywishlist = set("pizza")
print(mywishlist)
