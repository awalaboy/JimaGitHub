#msg= 'Jima has always been friendly with the locals.' 
#print(msg[-7]) 
#msg='welcome to Python 101: Strings'
#msg1= msg[-12]+' '+msg[:7]+' '+msg[25:29]+' '+msg[-6]+msg[4]+' '+msg[-6]+msg[12]+msg[2]+msg[1]+msg[-5]
#print(msg1[::-1])
#a=7
#b=3
#print('a == b is', a == b)
#print('a != b is', a != b)
#print('a > b is', a > b)
#print('a < b is', a < b)
#print('a >= b is', a >= b)
#print('a <= b is', a <= b)
#print('o in John is ','o' in 'John') #membership
#print('o in John is ','o' not in 'John') #non membership
#print('John is John ','John' is 'John') #identity
#print('John is not John is ','John' is not 'John') # negative identity 

#is_dark = False 
#is_tall = False 
#name = 'Joy' 
#print('Hello ' + name + ' how are you doing today?') 
#if is_dark and is_tall: 
#	print('The girl is very fine and sweet') 
#elif is_dark and not (is_tall): 
#	print('She is okay')
#else: 
#	print('The girl is just there')  

#amount = 149000 
#print('Hello Obarijima!') 
#if amount >= 150000: 
#	print ('Where una dey see this money from?') 
#else: 
#	print('Na God go help you my brother') 

#mode = input('Enter math operation(+,*,/,-): ') 
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#if mode == '+': 
#	print(f'Answer is : {num1 + num2}') 
#elif mode == '-' : 
#		print(f'Answer is : {num1 - num2}') 
#elif mode == '*' : 
#		print(f'Answer is : {num1 * num2}') 
#elif mode == '/' : 
#		print(f'Answer is : {num1 / num2}') 
#else: 
#	print('You have made an invalid entry.')
#guess = 0
#guess_limit = 5
#guess_number = 23 
#num = int(input("Enter a number: ")) 
#while guess < guess_limit: 
#	if guess != num:
#        guess_number + = 1
#if num == guess_number: 
#	print('Congratulations! You guessed right') 
#elif num > guess_number: 
#	print ('Entry too high, guess again within the range of 18 -  50 : ') 
#elif num < guess_number: 
#	print ('Entry too low, guess again 1 - 30 : ') 
#else: 
#	print ("Sorry, you lose") 
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
