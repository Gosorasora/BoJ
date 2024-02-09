import sys
input = sys.stdin.readline

dp = [[0 for j in range(1001)] for i in range(1001)]
N,M = map(int, input().split())
maxNum = 0

for i in range(0,N):
    matrix = list(input())
    
    for j in range(0,M):
        dp[i][j] = int(matrix[j]) # dp테이블에 값 하나씩 떼어와 입력
        
        if dp[i][j] == 1 and j>0 and i>0 :
            dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j]) + dp[i][j] #점화식 
        if maxNum < dp[i][j]:
            maxNum = dp[i][j]
            
print(maxNum*maxNum)