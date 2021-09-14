

a = [5,1,12]
b = [1,8,9]
c = [None]*4

a_len = len(a)
carry = 0
for x in range(a_len-1,-1,-1):

	digit_sum = a[x]+b[x]+carry
	if digit_sum<=9:
		c[x] = digit_sum

	else:

		digit , carry = digit_sum%10, digit_sum//10

		c[x] = digit
	#print( digit_sum , digit, carry )

print(c)