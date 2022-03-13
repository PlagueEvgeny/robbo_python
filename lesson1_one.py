num = [1, 2, 3, 4, 5]

print(num[1])

letters = list('Hello')


print(letters) 


people = ['Tom', 'Sam', 'Bob']
for person in people:
    print(person)


i = 0
while i < len(people):
    print(people[i])
    i += 1

##print(dir(people))
new_person = ['Robbo', 'Admin']
people.append('Alice')
print(people)
people.insert(0, 'Bill')
print(people)
people.extend(['Mike', 'Alex'])
print(people)
people.insert(0, new_person)
print(people)
people.remove('Alex')
print(people)
del people[0]

people.sort()
print(people)


numbers = [9, 24, 44, 2, 1, 55, 6, 14, 0]
numbers.sort()
print(numbers)
print(min(numbers))
print(max(numbers))
