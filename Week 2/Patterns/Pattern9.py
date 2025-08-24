Problem link - https://www.geeksforgeeks.org/problems/triangle-pattern-1661718013/1?page=1&category=pattern-printing&sortBy=submissions
Go ahead and solve the problem in GFG as well.

n = 4;
for i in range(1,n+1) :
    for j in range (1,i+1):
        print("*",end=" ");
    print("")
for i in range(1,n+1):
    for j in range(1,n-i+2-1):
        print("*", end=" ")
    print("")

Output:
*
* *
* * *
* * * *
* * *
* *
*
