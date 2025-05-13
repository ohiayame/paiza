# N、クラスの縦の席数 H、クラスの横の席数 W
ｎ, h, w = map(int, input().split())
table = []

sy, sx = map(int, input().split())
sy -= 1
sx -= 1
road = input()

ro = []

for r in road:
    if r == 'F' :
        sy -= 1
    elif r == 'B':
        sy += 1
    elif r == 'R':
        sx += 1
    else:
        sx -= 1
    
    ro.append([sy,sx])


for i in range(h):
    num = list(map(int, input().split()))
    table.append(num)  

for j in range(len(ro)):
    y = ro[j][0]
    x = ro[j][1]
    print(table[y][x])