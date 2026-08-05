def power(p, n):
    if n == 0:
        return 1
    else:
        return p * power(p, n - 1)


# Input
p = float(input("Enter Principal growth factor (P): "))
n = int(input("Enter number of years (n): "))

# Function call
result = power(p, n)
print("P^n =", result)
