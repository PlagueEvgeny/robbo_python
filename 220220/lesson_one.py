class Person:
    
    def __init__(self, name):
        print('Create objects Person')
        self.name = name
        self.age = 15
        
    def say_hello(self, message):
        print(message)

    def say(self):
        self.say_hello('Hello work')

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

tom = Person('Tomas')
tom.name = 'Spider-Man'
tom.say()
tom.display_info()

print(tom.name)
print(tom.age)

tom.age = 25
print(tom.age)

tom.company = "JetBrains"
print(tom.company)
