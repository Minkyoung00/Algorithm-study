# from itertools import combinations
# n, k = map(int, input().split())
# num = list(map(int, input()))
# max_val = 0

# for com in combinations(num, n-k):
#     val = int(''.join(map(str, com)))
#     if val > max_val:
#         max_val = val
# print(max_val)
    
    
n, k = map(int, input().split())
num = input()
remove = k
stack = []

for i in num:
    while remove > 0 and stack and stack[-1] < i:
        stack.pop()
        remove -= 1
    stack.append(i)
    
if remove > 0:
    stack = stack[:-remove]
    
print("".join(stack))
    