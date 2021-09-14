a = [25,3,21,5,7,8]
for x in range(0, len(a)):
	j = x
	while j>0 and a[j-1] < a[j]:
		a[j-1],a[j], = a[j],a[j-1]
		j-=1

print a