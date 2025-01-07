from collections import Counter
import sys
input = sys.stdin.read().split()

n = int(input[0])
a = list(map(int, input[1:n+1]))

a.sort()
total = sum(a)
avg = round(total / n)
mid = a[n//2]

rng = a[-1] - a[0]

dict = {}

# for num in a:
#     if num in dict:
#         dict[num] += 1
#     else:
#         dict[num] = 1
     
     
freq = Counter(a)   
max_freq = max(freq.values())

mode = [key for key, value in freq.items() if value == max_freq]

if len(mode) > 1:
    mode = sorted(mode)[1]
    
else:
    mode = mode[0]
# max_freq = max(dict.values())
# mode = []

# for key, value in dict.items():
#     if value == max_freq:
#         mode.append(key)
        
# if len(mode) > 1:
#     mode.sort()
#     mode = mode[1]
# else:
#     mode = mode[0]
print(avg)
print(mid)
print(mode)
print(rng)