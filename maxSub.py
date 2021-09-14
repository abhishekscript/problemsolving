


d 	= [-2,1,-3,4,-1,2,1,-5,4]

temp = 0
prev = d[0]
maxVal = 0


for i in range(0, len(d)):

	temp = temp+d[i]
	if temp>prev:
		prev = temp

	if temp < 0:
		temp = 0


print(  prev )
