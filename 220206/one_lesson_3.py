def print_messages():
    def say_hello(): print("Hello")
    def say_goodbye(): print("Good Bye")

    say_hello()
    say_goodbye()


##print_messages()


def main():
    say_hello()
    say_goodbye()

def say_hello():
    print("Hello")
def say_goodbye():
    print("Good Bye")

##main()

def say_name(name):
    print(f"Hello, {name}")

##say_name("Tom")
##say_name("Bob")

def say_person(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

##say_person(age = 45, name = "Bob")


def sum(*numbers):
    result = 0
    for n in numbers:
        result += n
    print(f"sum = {result}")

##sum(1, 23, 33, 66, 323, 434, 45677)
##sum(55, 45)








def double(number):
    return 2 * number

result1 = double(150)
result2 = double(1000)
print(f"result1 = {result1}")
print(f"result2 = {result2}")


def get_message():
    return "Hello RobboClub!"
    print("End of the function")

print(get_message())



def person(name, age):
    if age > 120 or age < 1:
        print("Invalid age")
        return
    print(f"Name: {name}\n Age: {age}")

person('Tom', 22)
person('Bob', 125)
