
hashMap ={
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}



decoded_data = []
s=input()
i=0
l=len(s)
num=0
decoded_data = [ hashMap[ x ]  for x in s]

#XVI
print(decoded_data)

num=0
l=len(decoded_data)
i = (l-1)
sum_=0
last_num=None

while i >= 0:
for i in range(k, 0, -1)
	#print(last_num)
	if last_num==None:
		last_num=decoded_data[i]
		sum_=last_num
	else:
		if last_num < decoded_data[i]:
			sum_+=decoded_data[i]
			last_num=decoded_data[i]

		elif last_num > decoded_data[i] :
			sum_-=decoded_data[i]
			last_num=decoded_data[i]
		elif last_num == decoded_data[i]:
			sum_+=decoded_data[i]
			last_num=decoded_data[i]

	print(sum_)
	i-=1
print(sum_)


