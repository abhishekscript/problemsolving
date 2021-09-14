



def squareRoot( num, left_ptr, right_ptr,target ):

	if left_ptr<right_ptr:

		mid = num//2
		mul = mid*mid
		ans = mid
		#print(mid, mul)
		if mul == target:
			return mid

		if target > mul :
			left_ptr = mid+1


			return squareRoot( mid, left_ptr, right_ptr, target  )
		else:
			right_ptr = mid-1
			
			return squareRoot(mid, left_ptr, right_ptr, target )
	else:
		return left_ptr

number = int(input())
target = number
low  = 0
high = 16

print(squareRoot( number, low, high, target ))