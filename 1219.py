import sys
input = sys.stdin.readline

N, S, E, M = map(int, input().split())
edges = []
D = [-sys.maxsize]*N

for _ in range(M):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))
    
Cost = list(map(int, input().split()))

D[S] = Cost[S]

for i in range(N+101): # 양수 사이클을 확인 하려면 충분히 큰수가 들어가야 하는데 N의 최대값이 100이라서 N+1 + 100
    for start, end, weight in edges:
        if D[start] == -sys.maxsize:
             continue
        elif D[start] == sys.maxsize:
             D[end] = sys.maxsize
        elif D[end]< D[start] + Cost[end] - weight :
            D[end] = D[start] + Cost[end] - weight
            if i >= N-1:
                D[end] = sys.maxsize
                
if D[E] == -sys.maxsize:
    print("gg")
elif D[E] == sys.maxsize:
    print("Gee")
else:
    print(D[E])
