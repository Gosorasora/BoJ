import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n,m = map(int, input().split())
parent = [0]*(n+1)

def find(Node):
    if Node == parent[Node]:
        return Node
    else:
        parent[Node] = find(parent[Node])
        return parent[Node]
    
def union(a,b):
    a = find(a)
    b = find(b)
    
    if a != b: #서로의 대표노드가 같지 않은 경우 
        parent[b] = a 

def isSame(a,b): #대표노드가 같은 지 확인하는 함수 
    a = find(a)
    b = find(b)
    
    if a == b :
        return True
    else:
        return False

for i in range(n+1):
    parent[i] = i
    
for i in range(m):
    trg,a,b, = map(int, input().split())
    if trg == 0:
        union(a,b)
    else:
        print("YES") if isSame(a,b) else print("NO")
                
    