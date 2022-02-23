n = int(input("Enter a value:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")
for i in range(n-1,0,-1):
    k=1
    for j in range(i,0,-1):
        print(k,end=" ")
        k+=1
    print("\n")
