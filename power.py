import math
class Solution:
	def myPow(self, x: float, n: int) -> float:
		if n==0:
			return 1
		temp=self.myPow(x,n//2 if n>0 else math.ceil(n/2))
		#ceil n/2 if n<0
		if n%2==0:
			return temp*temp
		else:
			if n<0:
				return temp*temp*(1/x)
			else:
				return temp*temp*x

#time complexity - O(logn)

#space complexity - O(1), no auxillary data structure used

#all test cases passed