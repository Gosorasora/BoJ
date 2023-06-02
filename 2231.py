N  = int(input())
N_len = len(str(N))

for i in range(N):
    num_list = list(map(int, str(i)))

    M = i
    for j in num_list:
        M +=j
    
    if M == N:
        print(i)
        break
else:
    print("0")
    
        

