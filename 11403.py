N = int(input())
D = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    D[i] = list(map(int, input().split()))
    
for k in range(N):
    for j in range(N):
        for i in range(N):
            if D[i][k] == 1 and D[k][j] == 1 :
                D[i][j] = 1

for i in range(N):
    for j in range(N):
        print(D[i][j], end = " ")
    print()