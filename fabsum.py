a=-1
b=1
s = 0
n = int(input("Enter how many fibanocci numbers you want:"))
for i in range(1,n+1):
        c=a+b
        print(c,end=' ')
        s=s+c
        a=b
        b=c
        i=i+1

print("\nThe sum of ",n," fibonacci numbers is:",s)
