H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

count = 0

for y in range(H):
    for x in range(W):
        for size in range(3, min(H, W) + 1):
            if y + size > H or x + size > W:
                continue

            ok = True
            for i in range(size):
                if grid[y][x+i] != '#' or grid[y+size-1][x+i] != '#':
                    ok = False
                if grid[y+i][x] != '#' or grid[y+i][x+size-1] != '#':
                    ok = False
            if not ok:
                continue

            dot_count = 0
            for i in range(1, size-1):
                for j in range(1, size-1):
                    if grid[y+i][x+j] == '.':
                        dot_count += 1

            if dot_count == 1:
                count += 1

print(count)