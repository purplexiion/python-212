class person:

    def read(self):
        self.name = input("Enter your name\n")
        self.age = input("Enter your age\n")
        self.height = input("enter your height\n")
        self.gender = input("enter your gender\n")
        self.weight = input("enter your weight\n")

    def write(self):
        # display class variables
        print(self.name, self.age, self.height, self.gender, self.weight)


# creating an object-instance of the class
p = person()
p1 = person()
# call the read and write methods
print("This is the first one")
p.read()
p.write()
print("This is the second one")
p1.read()
p1.write()
