N = int(input())

trees = list(map(int, input().split()))

# print(trees)

a = max(trees)
time = 0
count = 0
if a in trees:
    count += 1
if count >= 2:
    time = count-1

result = 1+N+time+1

print(result)
