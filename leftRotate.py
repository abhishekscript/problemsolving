

nums = [1,2]
k=int(input())



nums_len = len(nums)
if k  > nums_len:
	
	nums[:] = nums[ - nums_len :  ] + nums[  : -nums_len ]
	left_over = k % nums_len
	nums[:] = nums[ - left_over :  ] + nums[  : -left_over ]


else:
	nums[:] = nums[-k:]+nums[:-k]

print(nums)



'''
nums_len = len(nums)
if k > nums_len:
	rotations = [ nums_len ]
	while True:
		left_over = k - nums_len
		if left_over<=nums_len:
			rotations.append( left_over )
		k = left_over
		if k<nums_len:
			break
	for x in rotations:
		nums[:]=nums[-x:]+nums[:-x]
else:
	nums[:]=nums[-k:]+nums[:-k]

print(nums)

'''
