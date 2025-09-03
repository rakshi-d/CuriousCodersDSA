geeks for Geeks: problem Pattern 7
https://www.geeksforgeeks.org/problems/triangle-pattern-1661492263/1?page=1&category=pattern-printing&sortBy=submissions

N=int(input())
for i in range(1, N+1):
    for j in range(1, N-i+1):
        print(end=" ")
    for j in range(1,2*i):
        print("*",end="")
    print(" ")

Output:
N = 4 

      *
    * * *
  * * * * *
* * * * * * * 
