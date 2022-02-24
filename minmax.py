n = int(input("Enter size of list:"))
list = []
print("Enter elements in list:")
for i in range(n):
    x = int(input())
    list.append(x)
max = list[0]
for i in range(1,n):
    if list[i]>max:
        max=list[i]
print("Maximum value in list is:",max)
min = list[0]
for i in range(1,n):
    if list[i]<min:
        min=list[i]
print("Minimum value in list is:",min)
