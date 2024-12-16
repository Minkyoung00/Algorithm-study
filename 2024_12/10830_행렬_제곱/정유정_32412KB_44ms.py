import sys

N, B = map(int, sys.stdin.readline().strip().split())
origin = [[] for _ in range(N)]

for i in range(N):
    array = list(map(int, sys.stdin.readline().strip().split()))
    for j in array:
        origin[i].append(j % 1000)


def list_pow(a: list, exp: int) -> list:
    if exp == 1:
        return a

    ret = list_pow(a, exp // 2)
    ret = multiply(ret, ret)

    if exp % 2 == 1:
        ret = multiply(ret, origin)

    return ret


def multiply(o1: list, o2: list) -> list:
    global N

    ret =[[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                ret[i][j] += o1[i][k] * o2[k][j]
                ret[i][j] %= 1000

    return ret


result = list_pow(origin, B)
for row in result:
    print(' '.join(map(str, row)))
