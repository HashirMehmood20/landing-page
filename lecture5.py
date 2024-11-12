class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

p1 = Person("John", 36)
p1.display()
p2 = Person("Sara", 25)
p2.display()