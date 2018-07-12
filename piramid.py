n = int(input())
count = n
for i in range(n):
	count -= 1
	for j in range(count):
		print(" ",end="")
	for k in range(i):
		print('* ', end='')
	

	print('')
