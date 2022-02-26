n = int(input("Enter the size of list:"))
l = []
c = 0
print("Enter list elements:")
for i in range(n):
    x = int(input())
    l.append(x)
for i in range(n):
    if(l[i]!=0):
        c+=1
    else:
        del l[i]
print("The count of non zero elements is:",c)
print("The list elements are:",l)
