# create function
def main():
    print('Это простой калькулятор на Python')
    while True:
        print("Веберите действие которое хотите сделать: \n"
              "Сложить: +\n"
              "Вычесть: -\n"
              "Умножить: *\n"
              "Поделить: /\n"
              "Выйти: q\n")
        action = input('Действие: ')
        if action == 'q':
            print('Exit programms')
            break
        if action in ('+', '-', '*', '/'):
            x = float(input("x = "))
            y = float(input("y = "))

            if action == '+':
                print('%.2f + %.2f = %.2f' % (x, y, x+y))

            elif action == '-':
                print('%.2f - %.2f = %.2f' % (x, y, x-y))

            elif action == '*':
                print('%.2f * %.2f = %.2f' % (x, y, x*y))

            elif action == '/':
                if y != 0:
                    print('%.2f / %.2f = %.2f' % (x, y, x/y))
                else:
                    print('Деление на ноль!')
print(main())
        
