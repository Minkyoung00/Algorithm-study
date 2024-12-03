import sys

nums_size = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))

st = 0
end = nums_size - 1
mid = round(nums_size / 2) - 1

nums.sort()
ans = abs(nums[mid] - nums[end])

while mid < end:
    ans += abs(nums[end] - nums[st])
    end -= 1
    if mid < end:
        ans += abs(nums[st] - nums[end])
        st += 1

print(ans)
