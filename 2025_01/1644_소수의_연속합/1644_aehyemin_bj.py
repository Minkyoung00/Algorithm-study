import sys
input = sys.stdin.readline
n = int(input())

is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False


for i in range(2, int(n**0.5) + 1):
    if is_prime[i]:
        for j in range(i*2, n+1, i):
            is_prime[j] = False
prime = []

for k in range(n+1):
    if is_prime[k]:
        prime.append(k)
        




start = 0
end = 0

cnt = 0
num = 0

while start < len(prime):  # start가 범위를 벗어나지 않도록 조건 수정
    if num == n:
        cnt += 1
    if num >= n:
        num -= prime[start]
        start += 1
    elif end < len(prime):
        num += prime[end]
        end += 1
    else:
        break
  

print(cnt)