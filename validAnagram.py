

# valid anagram


s = input("first word\n")
t = input("second word\n")

hashMap = {}
flag = True
for x in s:
	if x not in hashMap:
		hashMap[x] = 1
	else:
		hashMap[x]+=1


for x in t:
	if x not in hashMap:
		print("Invalid anagram")
		exit(1)
		break

	hashMap[x]-=1


for x in hashMap:
	if hashMap[x]!=0:
		print("Invalid anagram")
		flag=False
if flag:
	print("valid")