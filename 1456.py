from collections import deque
import sys
input = sys.stdin.readline

N,M,K,X = map(int, input().split())
A = [[] for _ in range(N+1)]

ans = []
visited = [-1]*(N+1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] += 1 # 방문함을 알림 

    while queue:
        nowNode = queue.popleft()
        for i in A[nowNode]:
            if visited[i] == -1:
                visited[i] = visited[nowNode]+1 #방문했던 곳이라면 이곳에 몇번 째로 방문했음을 알 수 있다. and
                queue.append(i)

for _ in range(M): #인접 리스트 그리기 
    s,e = map(int, input().split())
    A[s].append(e)

BFS(X)

for i in range(N+1):
    if visited[i] == K:
        ans.append(i)

        
if not ans:
    print(-1)
else:
    ans.sort()
    for i in ans:
        print(i)
