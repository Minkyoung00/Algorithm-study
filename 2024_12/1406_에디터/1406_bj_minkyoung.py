from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()
    
text = input()
M = int(input())

left = deque(text)
right = deque()

for i in range(M):
  order = input().split()
  if order[0] == 'L':
    if left: right.appendleft(left.pop())
  elif order[0] == 'D':
    if right: left.append(right.popleft())
  elif order[0] == 'B':
    if left:
      left.pop()
  else:
    left.append(order[1])

print(''.join(left) + ''.join(right))

