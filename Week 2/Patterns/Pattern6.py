Write a Program which takes input n and prints the below pattern and upload the code to your github repo.
Sample 1:
Input:
n = 4
Expected output:
****
***
**
*
  
Sample 2
Input:
n= 6
******
*****
****
***
**
*

Solution:

n = int(input("Enter n: "))
for i in range(1,n+1) :
    for j in range (1,n-i+2):
        print("*",end="");
    print("")
    
