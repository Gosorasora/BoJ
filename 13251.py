D = [0]*51
probability = [0]*51
M = int(input())
D = list(map(int, input().split()))
total = 0

for i in range(0, M):
    total += D[i]
      
K = int(input())
ans = 0

for i in range(0, M):
    if D[i] >= K: #ex) 3개 뽑아야하는데 2개만 있는 경우 제외
        probability[i] = 1
        
        for k in range(0, K):
            probability[i] = probability[i] * (D[i] - K) / (total-k)
        ans += probability[i]

print(ans)


K = int(input())
ans = 0

for i in range(0, M):
    if D[i] >= K:
        probability[i] = 1
        for k in range(0, K):
            probability[i] = probability[i] * (D[i] - k) / (T - k)
        ans += probability[i]

print(ans)