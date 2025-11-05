divisible_by = 3*5
# 3*5 for div by 3 & 5
n = int(input("Min range: "))
m = int(input("Max range: "))
print(" ".join([str(i) for i in range(n + divisible_by - (n % divisible_by), m - (m % divisible_by) + 1, divisible_by)]))
