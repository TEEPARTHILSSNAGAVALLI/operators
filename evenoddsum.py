n = int(input("Enter upto how many numbers you want to print sum:"))
even = 0
odd = 0
for i in range(1,n+1):
    if(i%2==0):
        even = even + i
    else:
        odd = odd + i
print("Sum of ",n," even numbers is:",even)
print("Sum of ",n," odd numbers is:",odd)
