n, m = map(int, input().split())
results_li = [num for num in range(n)]

for _ in range(n):

    input_li = list(map(int, input().split()))
    
    results_li = [i for i in results_li if input_li[i] < m]
    
if len(results_li) > 0 :
    results_li = [str(idx + 1) for idx in results_li]
    print(" ".join(results_li))
else:
    print("wait")
