import heapq
n = int(input())
heap = []
for _ in range(n):
    gift = list(map(int, input().split()))
    a = gift[0]
    
    if a > 0 :
        for value in gift[1:]:
            heapq.heappush(heap, -value)
    else:
        if heap:
            print(-heapq.heappop(heap))
            
        else:
            print(-1)
