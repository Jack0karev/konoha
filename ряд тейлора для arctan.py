x = float(input())
res = 0
for n in range(500):
    res += (-1)**n * x**(2 * n + 1) / (2 * n + 1)
print(res)
