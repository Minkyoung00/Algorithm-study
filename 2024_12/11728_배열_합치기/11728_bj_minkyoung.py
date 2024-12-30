N ,M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = A + B

print(*sorted(result))