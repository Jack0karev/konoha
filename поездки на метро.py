a = int(input())
b = int(input())
n = int(input())
m = int(input())
l = max(n + (n - 1) * a, m + (m - 1) * b)
r = min(n + (n + 1) * a, m + (m + 1) * b)
if l <= r:
    print(l, r)
else:
    print(-1)

