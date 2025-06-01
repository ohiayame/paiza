n, m = map(int, input().split())

win_li = [0] * n

for i in range(m):
    win, loss = map(int, input().split())
    win_li[win-1] += win_li[loss-1]+1

for j in range(len(win_li)):
    if win_li[j] == max(win_li):
        print(j+1)
