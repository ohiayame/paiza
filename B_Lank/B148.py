n = int(input())
x_list = [int(input())for _ in range(n)]
indexed_list = [(val, idx) for idx, val in enumerate(x_list)]
sorted_li = sorted(indexed_list, reverse=True)
re = [""] * n

rank = 1
for i in range(n):
    val, idx = sorted_li[i]
    if i > 0 and val != sorted_li[i - 1][0]:
        rank = i + 1
    re[idx] = str(rank)

print("\n".join(re))