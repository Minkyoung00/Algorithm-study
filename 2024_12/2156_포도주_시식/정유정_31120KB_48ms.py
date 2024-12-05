import sys

wine_glasses = int(sys.stdin.readline())
wine_quantities = [0 for _ in range(wine_glasses + 1)]

for i in range(1, wine_glasses + 1):
    wine_quantities[i] = int(sys.stdin.readline())

dp = [0 for _ in range(wine_glasses + 1)]

if wine_glasses < 2:
    print(wine_quantities[1])

else:
    dp[1] = wine_quantities[1]
    dp[2] = dp[1] + wine_quantities[2]

    for i in range(3, wine_glasses + 1):
        dp[i] = max(dp[i - 1],
                    dp[i - 2] + wine_quantities[i],
                    dp[i - 3] + wine_quantities[i - 1] + wine_quantities[i])

    print(dp[wine_glasses])
