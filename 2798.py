#백준 2798번 블랙잭

M, N = map(int, input().split())
M_list = list(map(int, input().split()))

result = 0

for i in range(M):
    for j in range(i+1, M):
        for k in range(j+1, M):
            
            NewSum = M_list[i]+M_list[j]+M_list[k]
            
            if NewSum <= N:
                result = max(result, NewSum)

print(result)