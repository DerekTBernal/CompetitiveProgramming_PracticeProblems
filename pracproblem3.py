# assuming list is needed for problem
l = []
odd = 0
even = 0
for i in range(int(input("Enter list size: "))):
    print("List:") if i == 0 else None
    l.append(int(input()))
for i in l:
    odd += 1 if (i%2) == 1 else 0
    even += 1 if (i%2) == 0 else 0
print(f"Even numbers: {even}\nOdd numbers: {odd}")
