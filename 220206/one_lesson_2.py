num = 0
while num < 5:
    num += 1
    if num == 3:
        continue
    print(f"number = {num}")


def say_hello():
    
    return "Hello"


hello = say_hello()

say_hello()
print(hello)
