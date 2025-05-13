n = int(input())
max_num = int(n // 2)
sum = 0

for i in range(n):
    x = 0
    num = list(map(int, input().split()))
    for j in range(n):
        if i > max_num:
            if j + i < n :
                x += 1
            elif j + i >= i*2 +1:
                x -= 1
        else:   
            if j <= i :
                x += 1
            elif j + i >= n:
                x -= 1
        
        sum += num[j] - x 

print(sum)