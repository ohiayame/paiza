from re import S


n = int(input())

msg = ""
for i in range(n):
    msg += input()
    if(i < n-1):
        msg += ","
print(f"Hello {msg}.")