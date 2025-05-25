w, h, n = map(int, input().split())
x, y = map(int, input().split())

for i in range(n):
    dir_i, m_i = input().split()
    m_i = int(m_i)
    if  dir_i == "U":
        y += m_i
    elif dir_i == "D":
        y -= m_i
    elif dir_i == "R":
        x += m_i
    else:
        x -= m_i

x = (x + w) % w
y = (y + h) % h


# def mod(a, b):
#     return a - int(a / b) * b

# if x < 0:
#     x = w + mod(x, w)
# elif w <= x:
#     x = mod(x, w)
# if y < 0:
#     y = h + mod(y, h)
# elif h <= y:
#     y = mod(y, h)

print(x,y)