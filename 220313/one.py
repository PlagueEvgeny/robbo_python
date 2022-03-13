##open(file, mode)

#MODE
# r - read
# w - write
# a - append
# b - binary

##myfile = open('text.txt', 'r')
##try:
##    myfile.write("Hello, World!")
##except Exception as e:
##    print(e)
##finally:
##    myfile.close()



with open('one.txt', 'r') as file:
    content = file.readlines()
    print(content)
