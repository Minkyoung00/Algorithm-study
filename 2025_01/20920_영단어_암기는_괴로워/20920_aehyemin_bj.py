import sys 

n, m = map(int, input().split())
#길이가 m 이상인 단어만 외움움
d = {}
word = []
for i in range(n):
    a = sys.stdin.readline().rstrip()
    if len(a) >= m:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1

# 자주 나오는 단어순
# 알파벳 사전순
# 긴 단어순


#x[0]는 단어, x[1] 는 빈도스스
words = sorted(d.items(), key=lambda x: ( -x[1], -len(x[0]),  x[0] ))

for i, j in words:
    print(i)