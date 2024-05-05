from collections import deque

N = int(input())
A = [[] for _ in range(N + 1)]
D = [0] * (N + 1)
BuildTime = [0] * (N + 1)  # 시간
result = [0] * (N + 1)

for i in range(1, N + 1):
    inputList = list(map(int, input().split()))
    BuildTime[i] = inputList[0]
    index = 1

    while True:
        preTemp = inputList[index]
        index += 1
        if preTemp == -1:
            break
        A[preTemp].append(i)
        D[i] += 1

q = deque()

for i in range(1, N + 1):
    if D[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    for next in A[now]:
        D[next] -= 1
        result[next] = max(result[next], result[now] + BuildTime[now])

        if D[next] == 0:
            q.append(next)

for i in range(1, N + 1):
    print(result[i] + BuildTime[i])
