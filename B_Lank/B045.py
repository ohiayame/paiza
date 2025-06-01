import random

m, n = map(int, input().split())
formulas = set()

while m > 0:
    a = random.randint(1, 98)
    b = random.randint(1, 99 - a)
    s = f"{a} + {b} ="
    if s not in formulas:
        formulas.add(s)
        m -= 1

while n > 0:
    a = random.randint(1, 99)
    b = random.randint(0, a)
    s = f"{a} - {b} ="
    if s not in formulas:
        formulas.add(s)
        n -= 1

for s in sorted(formulas):
    print(s)
