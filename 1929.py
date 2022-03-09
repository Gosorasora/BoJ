#백준 1929번 소수찾기
import math

def primenumber(x):
    if x == 1:
        return False
    
    for i in range (2, int(math.sqrt(x))+1):     
        if x % i == 0:
            return False
    
    return True

m, n = map(int,input().split())

for i in range (m,n+1):
    if primenumber(i) == True:
        print(i)
        