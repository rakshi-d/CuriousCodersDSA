Problem link - https://www.geeksforgeeks.org/problems/print-the-kth-digit3520/0
Print the Kth Digit


SOLUTION:
class Solution:
    def kthDigit(self, a, b, k):
        # code here
        n=a**b
        count = 0
        while(n>0):
            ld = n%10;
            count = count + 1;
            if count==k:
                return ld
            n=n//10;

OUTPUT:
7

OR

n=23423573
k = 3
count = 0
while(n>0):
    ld = n%10;
    count = count + 1;
    if count==k:
        print(ld)  
    n=n//10;

OUTPUT:
5
