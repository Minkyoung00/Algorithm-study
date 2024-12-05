n = int(input())
w = []

for i in range(n):
    w.append(int(input()))

memo = [0] * n

for i in range(n):
    if i == 0:
        memo[i] = w[i]
    elif i == 1:
        memo[i] = w[i-1] + w[i]
    elif i == 2:
        memo[i] = max(w[i-2], w[i-1]) + w[i]
    else:
        memo[i] = max(max(memo[:i-1]) + w[i], max(memo[:i-2]) + w[i] + w[i-1])

print(max(memo))
        