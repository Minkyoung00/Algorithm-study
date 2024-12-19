import sys

size = int(sys.stdin.readline().strip())
stack = []

for _ in range(size):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))
