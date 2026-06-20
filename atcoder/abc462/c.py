n = int(input())

xx = []
yy = []

for _ in range(n):
    (x, y) = map(int, input().strip().split())
    xx.append(x)
    yy.append(y)

x_min = min(xx)
y_min = min(yy)
x_min_indexs = [i for i in range(len(xx)) if xx[i] == x_min]
y_min_indexs = [i for i in range(len(yy)) if yy[i] == y_min]
min_indexs = set(x_min_indexs) | set(y_min_indexs)

result = len(min_indexs)

x_min_y_min_index = min((i for i in x_min_indexs), key=lambda i: yy[i])
candidate1 = (xx[x_min_y_min_index], yy[x_min_y_min_index])
y_min_x_min_index = min((i for i in y_min_indexs), key=lambda i: xx[i])
candidate2 = (xx[y_min_x_min_index], yy[y_min_x_min_index])

# 浮いた点を探す
count = 0
for x, y in zip(xx, yy):
    if min(candidate1[0], candidate2[0]) < x < max(
        candidate1[0], candidate2[0]
    ) and min(candidate1[1], candidate2[1]) < y < max(candidate1[1], candidate2[1]):
        count += 1

result += count

print(result)
