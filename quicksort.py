

def quicksort( data ):
	
	left , center , right = [], [], []
	data_length = len(data)
	
	if data_length>0:
		pivot = data[ data_length/2 ]
		for x in data:
			if x < pivot:
				left.append(x)
			elif x > pivot:
				right.append(x)
			else:
				center.append(x)
	else:
		return data

	return quicksort( left ) + center + quicksort( right )

print( quicksort( [99,4,1,8,9,1,2,3,5,5] ) )