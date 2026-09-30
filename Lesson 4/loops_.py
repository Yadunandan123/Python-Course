n = int(input("Enter the number for whose sum you want to find:"))
sum = 0
for i in range(2, n+1):
    sum = sum + i
print("\nsum =", sum)