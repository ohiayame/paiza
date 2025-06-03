n, m = map(int, input().split())
price_li = []
for _ in range(n):
    price_li.append(list(map(int,input().split())))
x = int(input())

sum_price = 0
st_idxd = 0
for i in range(x):
    road, station_num = map(int, input().split())
    if i == 0:
        sum_price += price_li[road-1][station_num-1]
    elif st_idxd != station_num-1:
        if st_idxd >= station_num-1:
            sum_price += price_li[road-1][st_idxd] - price_li[road-1][station_num-1]
        else:
            sum_price += price_li[road-1][station_num-1] - price_li[road-1][st_idxd]
    st_idxd = station_num-1
print(sum_price)
