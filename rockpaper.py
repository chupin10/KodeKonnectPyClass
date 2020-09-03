import random

computeroption = random.randint(1, 3)
if computeroption == 1:
    computeranswer = 'rock'
if computeroption == 2:
    computeranswer = 'paper'
if computeroption == 3:
    computeranswer = 'scissors'

myanswer = input('What is your choice? ')

if (myanswer != 'paper') and (myanswer != 'rock') and (myanswer != 'scissors'):
    print('You didnt choose a real option!')

if (myanswer == 'rock'):
    if (computeranswer == 'rock'):
        print('Its a tie!')
    if computeranswer == 'paper':
        print('You lose!')
    if computeranswer == 'scissors':
        print('You win!')

if (myanswer == 'paper'):
    if (computeranswer == 'paper'):
        print('Its a tie!')
    if computeranswer == 'rock':
        print('You win!')
    if computeranswer == 'scissors':
        print('You lose!')

if (myanswer == 'scissors'):
    if (computeranswer == 'scissors'):
        print('Its a tie!')
    if (computeranswer == 'rock'):
        print('You lose!')
    if computeranswer == 'paper':
        print('You win!')
