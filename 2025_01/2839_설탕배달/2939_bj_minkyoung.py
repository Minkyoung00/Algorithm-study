N = int(input())
cnt_5 = 0
cnt_3 = 0

for i in range(N//5, -1, -1):
    if (N - 5*i) % 3 == 0:
        cnt_5 = i
        cnt_3 = (N - 5*i) // 3
        break

if cnt_5 + cnt_3 > 0:
    print(cnt_5 + cnt_3)
else:
    print(-1)

