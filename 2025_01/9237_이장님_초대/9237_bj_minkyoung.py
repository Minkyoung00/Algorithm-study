N = int(input())
ts = [int(i) for i in input().split()]
ts.sort(reverse=True)

cur, end = 0, 0

for t in ts:
    cur += 1
    end = max(end, cur + t)

print(end + 1)
