print ('Welcome to my computer quiz!')

playing = input('Do you want to play? ')
print(playing)

if playing.lower() != 'yes':
	quit() 

print("Ok! Let's play :)")
score = 0

answer = input('What is the biggest animal in the world? ')
if answer.lower() == 'blue whale':
	print('Correct!')
	score += 1
else:
	print('Not Correct!')

answer = input('What is the third color of the rainbow? ')
if answer.lower() == 'yellow':
	print('Correct!')
	score += 1
else:
	print('Not Correct!')

answer = input('What continent is China located in? ')
if answer.lower() == 'asia':
	print('Correct!')
	score += 1
else:
	print('Not Correct!')

answer = input('What is the study of life called? ')
if answer.lower() == 'biology':
	print('Correct!')
	score += 1
else:
	print('Not Correct!')

print('You got ' + str(score) + ' questions correct!')
print('You got ' + str((score / 4) * 100) + '%.')