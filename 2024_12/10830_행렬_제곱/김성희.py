import sys
input = sys.stdin.readline

N, B = map(int, input().split())

matrix = []
temp = []
for _ in range(N):
	matrix.append(list(map(int, input().split())))
	temp.append(list(matrix[-1]))

def mul(i, j, temp):
	ret = 0
	# 곱하기
	for idx in range(N):
		ret += temp[i][idx] * matrix[idx][j]
	return ret

result = [[0] * N for _ in range(N)]

for k in range(1, B):
	# temp를 result로 교체
	if k % 2:
		source = temp
		dest = result
	else:
		source = result
		dest = temp

	for i in range(N):
		for j in range(N):
			dest[i][j] = mul(i, j, source) % 1000

for d in dest:
	print(*d)

# 모듈러 연산