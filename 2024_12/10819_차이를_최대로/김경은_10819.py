n = int(input())
numbers = list(map(int, input().split()))

numbers.sort()

ans = 0
mid = n // 2

for i in range(mid):
    ans += numbers[n - i - 1] - numbers[i]

ans *= 2

if n % 2 == 1:
    ans -= min(numbers[mid] - numbers[mid - 1], numbers[mid + 1] - numbers[mid])
else:
    ans -= numbers[mid] - numbers[mid - 1]

# 결과 출력
print(ans)
