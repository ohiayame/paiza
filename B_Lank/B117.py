car = int(input())
min = 0
t = []
for i in range(car):
    num = int(input())
    if num == min+1 :
        min = num
    else :
        t.append(num)

c = 0
while (min < car):
    for j in range(len(t)):
        if t[j] == min+1 :
            min += 1
    c += 1
print(c)