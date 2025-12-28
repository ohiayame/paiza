# hight, width = map(int, input().split())

# a = [list(map(int, input().split()))for _ in range(hight)]
# b = [list(map(int, input().split()))for _ in range(hight)]


# for h in range(hight*2-1):
#     r = []
#     if(h == 0):
#         for w in range(width):
#             if(w !=0):
#                 r.append((a[0][w] + b[0][w-1]) //2)
#             r.append((a[0][w] + b[0][w]) //2)
#     elif(h == hight*2 -2):
#         for w in range(width):
#             if(w !=0):
#                 r.append((a[hight-1][w] + b[hight-1][w-1]) //2)
#             r.append((a[hight-1][w] + b[hight-1][w]) //2)
#     else:
#         for w in range(width):
#             if(w !=0):
#                 r.append((a[h][w] + b[h-1][w-1]) //2)
#             r.append((a[h][w] + b[h-1][w]) //2)
#     print(*r)



H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

for y in range(2 * H - 1):
    row = []
    ay = (y + 1) // 2
    by = y // 2
    for x in range(2 * W - 1):
        ax = (x + 1) // 2
        bx = x // 2
        row.append((A[ay][ax] + B[by][bx]) // 2)
    print(*row)
