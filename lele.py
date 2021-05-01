guess_number = 23 
num = int(input("Enter a number: ")) 
if num == guess_number: 
	print('Congratulations! You guessed right') 
elif num > guess_number: 
    print ('Entry too high, guess again within the range of 18 -  50 : ') 
elif num < guess_number: 
	print ('Entry too low, guess again 1 - 30 : ') 
else: 
	print ("Sorry, you lose!")
