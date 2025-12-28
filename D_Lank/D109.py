n = input()
num = n[0]
result = True
for i in range(1, len(n)):
    if(n[i] != " "):
        if num != n[i]:
            result = False

print("Yes" if result else "No")