n = int(input("Enter any number: "))
print(f"The sum of 1 to {n} is ", end="")
for i in range(n):
    n += i
print(n)
