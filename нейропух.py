import random as rd
n = int(input())
one = 0

both = 0
p = 3*10**5
for i in range(p):
    count = 0
    for k in range(n):
        learn = rd.uniform(a=0, b=3)
        gor = rd.expovariate(lambd=0.3)
        if learn > gor:
            count +=1
            gor2 = gor
    if count == 1:
        one +=1
    if gor2 <= 1 and count == 1:
            both += 1

print(both/one)
