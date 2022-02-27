string = '5'
num = 'hello'
number = int(string)
##number1 = int(num)
print(number)

##pr1 = input('number = ')
##p = int(pr1)
##print(p)


try:
    pr1 = 1
    print(f'number: {pr1}')
except KeyError:
    print('error')

finally:
    print('Блок завершился')

print('finish')


#BaseException
#Exception
#ArithmeticError
#BufferError
#LookupError

#IndexError
#KeyError
#OwerflowError
#TypeError
#ValueError
#ZeroDivisionError

##try:
##    number1 = int(input('print one numer: '))
##    number2 = int(input('print two numer: '))
##    if number2 == 0:
##        raise Exception('Второе число не должно быть нулем')
##    number12 = number1/number2
##    print(f'Результат деления: {number12}')
##except (Exception, ValueError) as e:
##    print(e)
##except BaseException:
##    print('Общее исключение')


class PersonAgeException(Exception):
    def __init__(self, age, minage, maxage):
        self.age = age
        self.minage = minage
        self.maxage = maxage

    def __str__(self):
        return f'Недопустимое значение: {self.age}. Возраст должен быть в диапозоне от {self.minage} до {self.maxage}'
    

class Person:
    def __init__(self, name, age):
        self.__name = name
        minage, maxage = 1, 110
        if minage < age < maxage:
            self.__age = age
        else:
            raise PersonAgeException(age, minage, maxage)

    def display_info(self):
        print(f'Name: {self.__name} Age:{self.__age}')


try:
    tom = Person('Tom', 37)
    tom.display_info()

    bob = Person('Bob', -10)
    bob.display_info()
    
except PersonAgeException as e: 
    print(e)





                  
