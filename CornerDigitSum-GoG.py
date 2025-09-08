Solve the below problem in geeksforgeeks - https://www.geeksforgeeks.org/problems/corner-digits1317/1
Corner Digit Sum

SOLUTION:
class Solution:
	def corner_digitSum(self, n):
		# Code here
		sum_ = n % 10
        count = 0
        while n > 0:
            if n == n % 10 and count >0:
                sum_ += n % 10
            count += 1
            n = n // 10
        return sum_
