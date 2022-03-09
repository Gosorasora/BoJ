#백준 2581번 소수찾기 
import math

def primenumber(x):
    if x == 1:
        return False
    
    for i in range (2, int(math.sqrt(x))+1):     
        if x % i == 0:
            return False
    
    return True

M = int(input())
N = int(input())
sum = 0
arr=[]

for i in range (M , N+1):
    if primenumber(i) == True:
        sum = sum + i #합 찾기
        arr.append(i)

if sum == 0:
    print(-1)
else:
    print(sum)
    print(arr[0])
