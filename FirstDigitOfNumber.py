n = int(input())
count = 0
while (n > 0):
    ld = n %10
    count = count + 1
    if(n==ld):
        print(ld)
    n = n //10
print(count)

OUTPUT:
12345
1
5
