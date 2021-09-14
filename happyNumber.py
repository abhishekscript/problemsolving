


def isHappy( n: int) -> bool:
	
	if n==1:
		return True
	

	def getSumOfDigits( n , visitedNumber):
		


		
		s = 0
		while n!=0:
			d = n%10
			n = n//10
			s = s+d*d
		
		if s==1:
			return s
		elif s in visitedNumber:
			return s
		else:
			visitedNumber.add( s )
			return getSumOfDigits(s, visitedNumber)
		
	visitedNumber = set()
	digit = getSumOfDigits(n, visitedNumber)
	if digit==1:
		return True
	return False


print( isHappy( 19 ) )