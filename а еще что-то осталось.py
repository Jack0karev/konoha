n_a = int(input())
A = list(map(int, input().split(" ")))

n_b = int(input())
B = list(map(int, input().split(" ")))

n_c = int(input())
C = list(map(int, input().split(" ")))

S = int(input())

def fast_algo(A,B,C,S):
    q = 0
    C = set(C)
    for i in range(len(A)):
        for j in range(len(B)):
            if S - A[i] - B[j] in C:
                q += 1
    return q

print(fast_algo(A,B,C,S))