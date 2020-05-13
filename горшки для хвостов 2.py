b=int(input())
a=list(map(int, input().split()))
a.sort()
c=b-3
d=0
for i in a:
    if i-c>=3:
        c=i
        d+=1
print(d)
