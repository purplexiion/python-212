def multipleseq():
    # make a loop that will print all numbers from one to 100
    count = 0
    y = 0
    for y in range(0,100):
        y = y + 1
        count = count + 1
        if y % 15 == 0:
            print("FizzBuzz")
        elif y % 5 == 0:
            print("Buzz")
        elif y % 3 == 0:
            print("Fizz")
        else:
            print(y)


multipleseq()
