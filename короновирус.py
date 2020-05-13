def get_neis(x, y):
    cnt = -field[y][x]
    for i in range(-1, 2):
        for j in range(-1, 2):
            cnt += field[y + i][x + j]
    return cnt


n, t = list(map(int, input().split()))
inf = 1000
field = [list(map(int, input().split())) + [0] for i in range(n)]
field = field + [[0 for i in range(n + 1)]]
new_field = [field[i][::] for i in range(n + 1)]
for i in range(t):
    for y in range(n):
        for x in range(n):
            neis = get_neis(x, y)
            if (neis < 2 or neis > 3):
                new_field[y][x] = 0
            if (neis == 3):
                new_field[y][x] = 1
    field = [new_field[i][::] for i in range(n + 1)]
for i in field[:-1]:
    print(*i[:-1])

