import numpy as np

print('Enter "q" whenever you want to quit!')

x = input('Enter number x : ')
if x == 'q':
	exit()
y = input('Enter number y : ')
if y == 'q':
	exit()

while True:
	x = int(x)
	y = int(y)

	power = x ** y
	log = np.log2(x)

	print('X**y = ' + str(power))
	print('log(X) = ' + str(log))

	print('Enter "q" whenever you want to quit!')
	x = input('Enter number x : ')
	if x == 'q':
		exit()
	y = input('Enter number y : ')
	if y == 'q':
		exit()
