import random

lowest_number = 0
biggest_number = 10

correct_answer = random.randint(lowest_number, biggest_number)

num_tries = 3

for count in range(num_tries):
    guess = int( input("Enter your guess: ") )
    if guess == correct_answer:
        print('You guessed the correct number!!!')
    else:
        print('Your answer was wrong!')

print('The correct answer was: {}'.format(correct_answer))
