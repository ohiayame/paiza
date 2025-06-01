h, w = map(int, input().split())
n, t = map(int, input().split())

set_li = [0] * (w * h)

for _ in range(n):
    i, j = map(int, input().split())
    set_li[(i-1) * w + j-1] += 1
set_li = sorted(set_li, reverse=True)
result = 0
for idx in range(t):
    if idx >= len(set_li):
        break
    result += set_li[idx]

print(result)