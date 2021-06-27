"""
The following program counts the number of times the letter a appears in a string:

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
This program demonstrates another pattern of computation called a counter. The variable count is initialized to 0 and then incremented each time an a is found.
When the loop exits, count contains the result: the total number of a's.

Exercise 3:
Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.
"""


def counta(word):
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
    return count  #


print(counta("orange"))
