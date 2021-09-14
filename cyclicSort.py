

d = [ 4,3,1,2 ]

left  = 0
right = len(d)
swap = 0
while left<right:

	if left+1 != d[ left ]:

		current = d[ left ]
		jump    = d[left]-1

		d[ left ], d[  jump  ]  = d[ jump ], d[ left ]
		swap+=1
	else:
		left+=1
print(d)
print(swap)