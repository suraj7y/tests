n = int(input())
count = 0
for i in range(n):
	count += 1
	if (i>0):
		for j in range(i):
			print(" ",end="")
	for k in range(i):
		if (i==3)and(k==2):
			print(" ",end="")
		print("*",end="")
	print('')
for i in range(n,0,-1):
	count -= 1
	if (i>0):
		for j in range(count):
			print(" ",end="")
	for k in range(i):
		print("*",end="")
	print('')
