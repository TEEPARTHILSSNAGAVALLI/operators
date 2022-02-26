n = int(input("Enter size of list:"))
list=[]
print("Enter list elements:")
for i in range(n):
    x = int(input())
    list.append(x)
for i in range(n):
    for j in range(i+1,n):
        if(list[i]<list[j]):
            t = list[i]
            list[i] = list[j]
            list[j] = t
print("The list elements are:",list)
