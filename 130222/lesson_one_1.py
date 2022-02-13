message = lambda: print('''Hello
world''')

def message():
    print('hello')


message()


square = lambda n: n * n

print(square(4))


def do(a, b, oper):
    result = oper(a, b)
    print(f'result = {result}')


do(5, 4, lambda a, b: a + b)



a = '2'
b = int(True)
c = int(a) + b
print(type(a))
print(type(b))
print(type(c),f'{a} + {b} = {c}')



