n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

def binarySearch(target):
    left = 0
    right = n - 1
    
    while(left <= right):
        mid = (left + right) // 2 # / 사용시 실수형으로 되기 때문에 // 사용
        
        if (n_list[mid] == target):
            return True
        
        elif(n_list[mid] > target):
            right = mid - 1
        else:
            left = mid + 1

for i in range(m):
    if binarySearch(m_list[i]) :
        print(1)
    else:
        print(0)
    
#시간 초과로 인해 이진탐색으로 풀어야한다.
# for i in range(m):
#     for j in range(n):
#         if m_list[i] == n_list[j]:
#             result[i] = 1
#             continue
#     print(result[i])