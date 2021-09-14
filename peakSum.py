





'''
data.sort()

left,right=0,len(data)-1
while True:
	s = data[left] + data[right]
	if s == target:
		print(s, target)
		#print(data[left], data[right])
		print(data[left], data[right], " values")
		print(left, right, " index")
	
	if s>target:
		right-=1
	elif s<=target:
		left+=1

	if left>=right:
		break
'''
3

{
	3 : 0,
	4 : 1,
	5 : 2,
	
}

data=[3,2,1,4]
target = 6

hashMap = {}
for index,x in enumerate(data):
	complement = target - x
	if x in hashMap:#.get( x )==None and complement>0:
		print(hashMap[x], index)# = index
	else:
		hashMap[complement]=index



#print(hashMap)