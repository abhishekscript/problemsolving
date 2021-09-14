


#UN-ORDERED APPROACH
s =  ["flower", "flow", "flight"] 


data = [ set(x) for x in s ]
i= 1
l= len(data)
prev= data[0]
while i < l:

	temp = data[i].intersection( prev )
	prev = data[i]
	data[i] = temp
	i+=1
print( min(data))


#Ordered APPROACH
s = list(set([ "ab", "a" ]))
mxv = len( s[0] )
mxi = 0
i=0
for x in s:
	l=len(x)
	if l<mxv:
		mxv=l
		mxi=i
	i+=1
temp = s[mxi]
lk = len(temp)

for i in range(len(s)):
	if i!=mxi:
		k = s[i]
		for j in range( lk ):
			if  temp[j] !=k[j]:
				temp = temp[:j]
				lk = len(temp)
				break
print(temp)