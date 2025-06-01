n, k = map(int, input().split())

price_li = []
min_idx_li = [0] * k
for shop_idx in range(n):
    input_li = list(map(int, input().split()))
    for vege_idx in range(k):
        if shop_idx != 0 and input_li[vege_idx] < price_li[vege_idx]:
            price_li[vege_idx] = input_li[vege_idx]
            min_idx_li[vege_idx] = shop_idx
        elif shop_idx == 0 :
            price_li.append(input_li[vege_idx])
print(len(set(min_idx_li)))