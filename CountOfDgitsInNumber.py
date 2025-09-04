To print the last digits and total no of digits

n=23423573
count = 0
while(n>0):
    ld = n%10
    print(ld)
    count = count + 1
    n=n//10
print(count)

OUTPUT:
3
7
5
3
2
4
3
2
8  #total number of digits


OR


To print the last digits or reverse the number

n=23423573
while(n>0):
    ld = n%10
    print(ld)
    n=n//10

OUTPUT:
3
7
5
3
2
4
3
2
