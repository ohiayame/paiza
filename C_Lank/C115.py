n, m = map(int, input().split())
r = 0
for i in range(n-1):
    a = int(input())
    if(a <= m):
        r += a

print(r)