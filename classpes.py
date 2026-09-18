class stundent:
    grade = 10
    name = "Umar"

    def introduction(self):
        print("hi, I am student")

    def details(self):
        print("My name is", self.name)
        print("I am in grade", self.grade)

        ob = stundent()
        ob.introduction()
        ob.details()