N, M = map(int, input().split())
knowP = list(map(int, input().split()))
T = knowP[0]
del knowP[0]

result = 0
party = [[]for _ in range(M)]

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a != b:
        parent[b] = a
        
def isSame(a,b):
    a = find(a)
    b = find(b)
    
    if a == b :
        return True
    else:
        return False

for i in range(M):
    party[i] = list(map(int, input().split()))
    del party[i][0]
    
