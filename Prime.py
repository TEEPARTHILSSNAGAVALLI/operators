t = int(input())
c=0
s=0
for i in range(t):
    n = input()
    n = int(n)
    for j in range(2,n+1):
        for k in range(1,j+1):
             if i%j==0:
                 c=c+1
        if c==2:
             s=s+1
        c=0
    print(s)
