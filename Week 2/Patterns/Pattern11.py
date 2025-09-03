N=int(input())
for i in range(1, N+2):
    for j in range(1, i):
        print(end="  ")
    for j in range(1,(2*N)-(2*i)+2):
        print("*",end=" ")
    print(" ")

Output:
N=4
* * * * * * *
  * * * * *
    * * *
      *
