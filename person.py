class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hi, my name is {self.name}. I am {self.age} years old and my gender is {self.gender}.")

# Create an instance of Person
person1 = Person("denis", 22, "Female")

# Call the introduce method
person1.introduce()