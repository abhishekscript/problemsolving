def mergeSort(data):

	l = len(data)
	if l<2:
		return data

	mid = l//2
	left  = data[ :mid]
	right = data[ mid:]
	mergeSort(left)
	mergeSort(right)

	i = j = k = 0
	left_len  = len(left)
	right_len = len(right)
	
	while i < left_len and j < right_len:

		if left[i] < right[j]:
			data[k] = left[i]
			i+=1
		else:
			data[k] = right[j]
			j+=1
		k+=1

	while i < left_len:
		data[k] = left[i]
		k+=1
		i+=1

	while j < right_len:
		data[k] = right[j]
		k+=1
		j+=1

data = [5,6,1,24,-1,0]
mergeSort(data)
print(data)