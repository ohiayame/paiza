n, m = map(int, input().split())

if(n % 2 == 0):
    if(m % 2 != 0):
        print('YES')
    else:
        print('NO')
elif(m % 2 == 0):
    if(n % 2 != 0):
        print('YES')
    else:
        print('NO')
else:
    print('NO')