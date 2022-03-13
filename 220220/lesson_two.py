class Person:
    def __init__(self, name):
        self.__name = name
        self.__age = 1

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 1 < age < 110:
            self.__age = age
        else:
            print('Error age')

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Name: {self.__name} \t Age: {self.__age}")

class Employee(Person):

    def work(self):
        print(f"{self.name} works")

tom = Employee("Tim")
print(tom.name)
tom.__age = 43
tom.display_info()
tom.age = -333
tom.age = 28
tom.display_info()
tom.__age = 43
print(tom.__age)
print(tom.work())


