

def seq( numbers ):
	if numbers == []:
		return [[]]

	x = seq( numbers[1:] )

	y = x + [[numbers[0]] + y for y in x ]
	print("finally",print(y))
	return y

seq( [1,2,3,4] )


def powerSet( numbers ):

	powerSet = [[]]

	for element in numbers:

		for subset in powerSet:
			powerSet = powerSet + [ list(subset) + [element] ]

	print(powerSet)
print("difference power set")
powerSet( [1,2,3,4] )
