n, a, b = map(int, input().split())

for i in range(1, n+1):
    r = ""
    if(i % a != 0 and i % b != 0):
        r = "N"
    if(i % a == 0):
        r = "A"
    if(r != "N" and i % b == 0):
        r += "B"

    print(r)