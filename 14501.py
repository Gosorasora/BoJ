import sys
input = sys.stdin.readline

N = int(input())
T = [0]*(N+1) # 상담완료 기간
P = [0]*(N+1) # 상담 시 얻는 이익

canBook = [True]*(N+1)

for i in range(1,N+1):
    T[i], P[i] = map(int, input().split())

