


d = [  1,2,3,4,5,9,12  ]



def iterativeBinary( target ):
	left   =0 
	right  =len(d)-1

	while left<=right:
		


		mid = (left + right)//2

		print( d[left],  d[mid], d[right] )

		if d[mid] == target:
			print( mid )
			break

		elif target >= mid:
			left = mid+1
		elif target <= mid:
			right = mid-1



iterativeBinary( 9 )


'''

def binarySearch( data , target):
	
	l = len(data)

	if l<=1:
		if data[0] == target:
			return 0
		return -1

	mid = l//2
	#print( data[mid], target )
	if data[ mid ] ==  target:
		return mid
	
	elif  target >= data[mid]:
		right = binarySearch( data[ mid: ],target )
		if right == -1:
			return right
		return right + mid

	elif target <= data[mid]:
		left = binarySearch( data[ :mid ],target )
		if left == -1:
			return left
		return mid - left

pos = binarySearch(d ,1) 
if pos>=0:
	print(pos)
else:
	print( "No element" )
'''