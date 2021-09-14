


nums= [
		[ 1,2,4,3 ],
		[ 4,1,1,5 ],
		[ 7,1,2,6 ]
]

def rotate( single_dimension ):
	
	left_ptr  = 0
	right_ptr = len(single_dimension)-1

	while left_ptr<right_ptr:
		single_dimension[left_ptr], single_dimension[right_ptr] = single_dimension[right_ptr],single_dimension[left_ptr]
		left_ptr+=1
		right_ptr-=1

	return  single_dimension



for x in nums:
	print(rotate( x ))