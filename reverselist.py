n = int(input("Enter size of list:"))
l1 = []
print("Enter elements into list:")
for i in range(n):
    x = int(input())
    l1.append(x)
l2 = []
t = n-1
for j in range(0,n,1):
    l2.append(l1[t])
    t=t-1
print("Reverse list is:\n",l2)
