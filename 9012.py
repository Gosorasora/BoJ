n = int(input())

for i in range(n):
    s = input()
    stk = []

    for ch in s:
        if ch == "(":
            stk.append(ch)

        elif ch == ")":
            if stk:
                stk.pop()
            elif not stk:
                print("NO")
                break
    else:
        if not stk:
            print("YES")
        else:
            print("NO")
        
        
