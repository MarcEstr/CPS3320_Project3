#This program is designed to make a randomized password with the length of 8.
import random


#Using ASCII, the program will generate a password with 3 Uppercase letters, 3 Lowercase letters, and 2 Numbers.
upperLetter1 = chr(random.randint(65,90))
upperLetter2 = chr(random.randint(65,90))
upperLetter3 = chr(random.randint(65,90))

lowerLetter1 = chr(random.randint(97,122))
lowerLetter2 = chr(random.randint(97,122))
lowerLetter3 = chr(random.randint(97,122))

num1 = chr(random.randint(48,57))
num2 = chr(random.randint(48,57))

#After generating numbers, we need to write the function to shuffle them in any order.
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

#Generate the password, then shuffle the order.
password = upperLetter1 + upperLetter2 + upperLetter3 + lowerLetter1 + lowerLetter2 + lowerLetter3 + num1 + num2
password = shuffle(password)

#print the randomly generated password.
print(password)

