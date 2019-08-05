import random
print('I am thinking of a number between 1 and 20.')
myNumber = random.randint(1, 20)
count = 0
youLose = False
while True:
	try: 
		number = int(input('Guess the number: '))
	except:
		print('Please try to enter an integer.\nRead about integers -> https://www.mathsisfun.com/definitions/integer.html')
		continue
	count += 1
	if number < myNumber:
		print('You are thinking too low.')
	elif number > myNumber:
		print('You are thinking too high.')
	elif number == myNumber:
		print('It took you', count, 'guesses to guess my number.')
		break
	lost = input('Say "i give up" for giving up, or just press enter to continue\n')
	if lost.upper() == 'I GIVE UP':
		youLose = True
		break
if youLose:
	print('My guess was', myNumber, ', Dumbo!')
