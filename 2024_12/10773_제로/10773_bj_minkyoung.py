from collections import deque
import sys
input = sys.stdin.readline

note = deque()
k = int(input())

for i in range(k):
    num = int(input())
    if num: note.append(num)
    else: note.pop()

print(sum(note))