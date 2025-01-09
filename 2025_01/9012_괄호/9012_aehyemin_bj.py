T = int(input())
result = []
for i in range(T):
    a = input().strip()
    stack = []

    
    for char in a:
        if char == '(':
            stack.append(char)
        elif not stack:
            result.append("NO")
            break
        else:
            stack.pop()
    else:
        if not stack:
            result.append("YES")
        else:
            result.append("NO")
print("\n".join(result))