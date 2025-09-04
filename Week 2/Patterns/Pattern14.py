Write a Program that takes input n and prints the below pattern and upload the code to your github repo.
Sample 1:
Input:
n = 8
Expected output:
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
6 6 6 6 6 6 
7 7 7 7 7 7 7 
8 8 8 8 8 8 8 8 
Sample 2
Input:
n= 6
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
6 6 6 6 6 6 
Hint: Check pattern 13 and think in terms of using count.

SOLUTION:
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()
