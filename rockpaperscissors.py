import random

computerchoice = random.randint(0, 2)
if computerchoice == 0:
    computerchoice = 'rock'
if computerchoice == 1:
    computerchoice = 'paper'
if computerchoice == 2:
    computerchoice = 'scissors'

print(computerchoice)

yourchoice = input('Enter rock, paper, or scissors: ')
if yourchoice == computerchoice:
    print("It's a tie! Try again.")

if yourchoice == 'rock':
    if computerchoice == 'paper':
        print('You lose!')
    if computerchoice == 'scissors':
        print('You win!')

if yourchoice == 'paper':
    if computerchoice == 'scissors':
        print('You lose!')
    if computerchoice == 'rock':
        print('You win!')

if yourchoice == 'scissors':
    if computerchoice == 'rock':
        print('You lose!')
    if computerchoice == 'paper':
        print('You win!')
