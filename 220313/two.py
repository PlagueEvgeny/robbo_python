FILENAME = 'messages.txt'

messages = []

for i in range(4):
    message = input('' + str(i+1) + ': ')
    messages.append(message + '\n')

with open(FILENAME, 'a') as file:
    for message in messages:
        file.write(message)

print("Сообщения:")
with open(FILENAME, 'r') as file:
    for message in file:
        print(message, end="")
