alphabet = {chr(el) for el in range(ord('а'), ord('я') + 1)}
alphabet.update([chr(el) for el in range(ord('А'), ord('Я') + 1)])
alphabet.update(['ё', '-'])
print(alphabet)

def name_is_valid(name):
    if not name:
        return False

    return name.istitle()

print(name_is_valid('Иван'))
print(name_is_valid('Иван-Костя'))
print(name_is_valid('ИВАН'))

assert not name_is_valid('ИВАН')
assert name_is_valid('ИВАН')
