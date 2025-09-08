n = int(input())
count = 0
while (n > 0):
    ld = n %10
    if(n%2!=0):
        count = count + 1
    n = n //10
print(count)

OUTPUT:
12345
3
