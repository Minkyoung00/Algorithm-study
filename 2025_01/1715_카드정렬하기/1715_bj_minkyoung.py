from queue import PriorityQueue 

N = int(input())
queue = PriorityQueue()
for i in range(N):
    queue.put(int(input())) 

result = 0
while not queue.empty():
    a = queue.get()
    b = queue.get()
    result += a+b
    queue.put(a+b) 

print(result)
