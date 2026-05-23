import sys

h, w = input().split()
h = int(h)
w = int(w)

result = [[4] * (w + 1) for _ in range(h + 1)]

if h == 1 and w == 1:
    print(0)
    sys.exit()

if h == 1:
    result = [2] * w
    result[0] = 1
    result[-1] = 1
    print(*result)
    sys.exit()

if w == 1:
    for i in range(h):
        if i == 0 or i == h - 1:
            print(1)
            continue
        print(2)

    sys.exit()


for i in range(1, h + 1):
    for j in range(1, w + 1):
        if (
            (i == 1 and j == 1)
            or (i == h and j == 1)
            or (i == 1 and j == w)
            or (i == h and j == w)
        ):
            result[i][j] = 2
            continue
        if i == 1 or i == h or j == 1 or j == w:
            result[i][j] = 3


for line in result[1:]:
    print(*line[1:])
