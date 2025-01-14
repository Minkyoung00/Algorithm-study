n = int(input())
nums = list(map(int, input().split()))

left = [0] * n
right = [0] * n

for i in range(n):
    if i == 0:
        left[i] = nums[i]
    else:
        left[i] = max(left[i-1] + nums[i], nums[i])

for i in range(n-1, -1, -1):
    if i == n-1:
        right[i] = nums[i]
    else:
        right[i] = max(right[i+1] + nums[i], nums[i])

result = max(left)

for i in range(1, n-1):
    result = max(result, left[i-1] + right[i+1])

print(result)
