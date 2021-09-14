atm = [2000, 500, 100, 50, 20, 10]

amount = 5200
k = 0

stack = []

while amount!=0:
	d = amount % atm[k]
	changes = amount // atm[k]
	amount = d
	stack.append( ( changes ,'*', d) )
	k+=1

print(stack)