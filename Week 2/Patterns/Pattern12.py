n=int(input())
for i in range(1,n):
    for j in range(1,n-i+1):
        print(end="  ")
    for j in range(1,2*i):
        print("*",end=" ")
    print(" ")
for i in range(1, n+2):
    for j in range(1, i):
        print(end="  ")
    for j in range(1,(2*n)-(2*i)+2):
        print("*",end=" ")
    print(" ")

Output:
n = 4
      *
    * * *
  * * * * *
* * * * * * *
  * * * * *
    * * *
      *


