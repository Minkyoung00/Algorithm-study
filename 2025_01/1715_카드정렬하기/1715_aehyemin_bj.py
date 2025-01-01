import heapq
n = int(input())

heap = []
for i in range(n):
    heapq.heappush(heap, int(input()))
    
    

cnt = 0
while len(heap) > 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    
    plus = one + two
    
    cnt += plus
    
    heapq.heappush(heap, plus)
    
print(cnt)
    
    