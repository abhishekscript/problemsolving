


n = 8

target = n

steps = [ 3,2,1 ]

step = 1

k = 0

w = []

while n!=0:

	d = n % steps[k]
	n = n//2
	left_over = target - ( n* steps[k] )
	print(n, left_over, steps[k])
	if d!=0:
		k+=1


	#print( [2]*n + [1]*left_over )