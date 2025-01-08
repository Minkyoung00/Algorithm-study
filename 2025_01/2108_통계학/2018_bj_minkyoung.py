import sys
from collections import Counter

input = sys.stdin.read().split()

N = int(input[0])
nums = list(map(int, input[1:]))

nums.sort()

cnt_nums = Counter(nums)
most_common = cnt_nums.most_common()
freq_n = []

for k,v in most_common:
    if v == most_common[0][1]:
        freq_n.append(k) 

if len(freq_n) > 1:
    freq_n.sort()
    freq_n = freq_n[1]
else:
    freq_n = freq_n[0]

print(round(sum(nums) / N)) 
print(nums[N // 2])         
print(freq_n)               
print(nums[-1] - nums[0])    