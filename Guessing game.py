from random import randint
print('I came up with a number from 1 to 10')
number = randint(1,10)
for _ in range(10000000):
    gues = int(input('Make your gues :'))
    if gues < number: print('The number is larger')
    if gues > number: print('The number is smaller')
    if gues == int(number):
      print('You have successfully guessed the number')
