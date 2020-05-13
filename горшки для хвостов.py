n = int((input()))
array = list(map(int, input().split()))
array = sorted(array)
i = 0
while i< len(array) and array[i]+1<=n:
    i+=1
if i< len(array):
    ans = 1
    max_leg = array[i]
    for j in range(i, len(array)):
        if array[j]>=max_leg + 3:
            max_leg = array[j]
            ans += 1
    print(ans)
else:
    print(0)

