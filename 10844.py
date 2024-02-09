import sys
input = sys.stdin.readline
mod = 1000000000

N = int(input())
dp = [[0]*11 for i in range(N+1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2,N+1):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][9]
    
    for j in range(1,9):
        dp[i][j] = (dp[i-1][j-1]+ dp[i-1][j+1]) % mod

sum = 0

for i in range(10):
    sum = (sum + dp[N][i])%mod
    
print(sum%mod)

