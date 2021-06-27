name = input('Enter:')
print(name)

fruit = "banana"
letter = fruit[1]
print(letter)

# Length - len() function
charNum = len(fruit)
print(charNum)

# while loop for a string
index = 0
while index < len(fruit):
    character = fruit[index]
    print(character)
    index += 1

for item in fruit:
    print(item)

# slicing stings
s = 'Studypug'
print(s[0:5])

# slicing from beginning
print(s[:5])
# slicing to the end
print(s[:5])

# in as an operator (boolean expression result)
if 'n' in fruit:
    print('n is found in ' + fruit)
else:
    print('n is not found in ' + fruit)
if 'm' in fruit:
    print('m is found in ' + fruit)
else:
    print('m is not found in ' + fruit)

stuff = 'Hello World'
print(type(stuff))
# display available string object methods
print(dir(stuff))

# find position of string
i = fruit.find("na")
print(i)
