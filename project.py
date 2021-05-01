num = 23
guess = 0
guess_limit = 3
guess_number = 0
guess = int(input(f'Guess a number 1-50: '))
guess_number += 1
while guess_number < guess_limit:
    
    if guess != num:
        guess_number += 1
        if guess > num:
            guess = int(input(f'{guess} Too high - Guess again 20 - 50: '))
        else:
            guess = int(input(f'{guess} too low - Guess again 1 - 40: '))
    if guess == num:
        print(f'You Win! You Guessed it: {guess}')
        break
    
if guess != num:
    print(f'Sorry you lose! It was {num}')
