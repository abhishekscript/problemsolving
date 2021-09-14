




def bsearch(  target ):

	left = 0 
	right = target


	while left<=right:

		mid = (left+right)//2

		square = mid*mid

		if square == target:
			print(mid)
			break

		elif target >=square:
			left = mid+1

		elif target <=square:
			right = mid-1

	print(left, right)

bsearch(  8   )