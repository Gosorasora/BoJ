import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
D = [[sys.maxsize for j in range (N+1)]  for i in range (N+1)]

for i in range(1, N+1):
    D[i][i] = 0
    
for i in range(M):
    s, e, v = map(int, input().split())
    if D[s][e] > v:
        D[s][e] = v
        
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if D[i][j] >  D[i][k] + D[k][j]:
                D[i][j] = D[i][k] + D[k][j]
                
for i in range(1, N+1):
    for j in range(1,N+1):
        if D[i][j] == sys.maxsize:
            print(0, end = " ")
        else:
             print(D[i][j], end = " ")
    print()
