def dfs(lott, num):
    if lott == 6:
        print(*ans)
        return

    for i in range(num, k):
        ans.append(s[i])
        dfs(lott + 1, i + 1)
        ans.pop()

while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    s = arr[1:]
    ans = []
    dfs(0, 0)
    print()
    if k == 0:
        exit()