x=7

for i in range(x-1):
	for j in range(i,x):
		print(' ',end='')
	for j in range(i+1):
		print('# ', end='')
	print()
	
for i in range(x):
	for j in range(i+1):
		print(' ',end='')
	for j in range(i,x):
		print('# ',end='')
	print()





