"""
Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string,
printing each letter on a separate line, except backwards.

Another way to write a traversal is with a for loop:

for char in fruit:
    print(char)
Each time through the loop, the next character in the string is assigned to the variable char. The loop continues until no characters are left.

"""

fruit = 'orange'
# the len function returns the number of characters in the string
# use -1 in order to bring the range to be inbounds
index = len(fruit) - 1

while index >= 0:
    print(fruit[index])
    index -= 1
