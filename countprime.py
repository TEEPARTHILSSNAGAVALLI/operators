n = int (input("Enter upto which number you want prime numbers:"))
c = 0
sum = 0
for i in range(2,n+1):
    for j in range(1,i+1):
        if i%j==0:
            c = c+1
    if c==2:
        print(i,end=' ')
        sum = sum+1
    c=0
print("\nNumber of prime numbers below ",n,"is :",sum)
