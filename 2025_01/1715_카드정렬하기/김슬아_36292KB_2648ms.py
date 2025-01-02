import heapq

N = int(input())

nums = [int(input()) for _ in range(N)]

heapq.heapify(nums)

result = 0

while len(nums) > 1:
    num_1 = heapq.heappop(nums)
    num_2 = heapq.heappop(nums)
    cost = num_1+num_2
    result += cost
    heapq.heappush(nums, cost)


print(result)
