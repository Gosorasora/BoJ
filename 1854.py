import sys
import heapq    
input = sys.stdin.readline

N, M, K = map(int, input().split())
myList = [[] for _ in range(N+1)] #인접 리스트 
distance = [[sys.maxsize]*K for _ in range(N+1)] #거리 리스트
#해당 경우에는 최단거리만 구하는 것이 아니기 때문에 visited 리스트가 필요 없음. 

for _ in range(M): #연결리스트 생성 
    a,b,c = map(int, input().split())
    myList[a].append((b,c))

hq = [(0,1)]
distance[1][0] = 0 #거리 초기화 

while hq :
    weight, city = heapq.heappop(hq)
    for newCity, newWegiht in myList[city]:
        if newWegiht + weight < distance[newCity][K-1]: #새롭게 알아낸 경로가 기존에 distance에 저장된 값보다 더 효율적(작을) 때
            distance[newCity][K-1] = newWegiht + weight #거리리스트의 row는 0~K-1까지 있으니 가장 마지막에 넣고 정렬.
            distance[newCity].sort()
            heapq.heappush(hq, [newWegiht + weight, newCity])
    

for i in range(1,N+1):
    if distance[i][K-1] == sys.maxsize:
        print(-1)
    else:
        print(distance[i][K-1])