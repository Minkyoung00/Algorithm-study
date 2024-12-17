import sys
input = sys.stdin.readline

# N 명의 학생
# M 가지 색상
N, M = map(int, input().split())

count = []
for _ in range(M):
	count.append(int(input()))

student = [0] * N

standard = min(count)
# student[0] = standard
# N -= 1

# 반복
if standard * N > sum(count):
	# 가능
	pass

standard -= 1

# standard 기준 학생 계산
# 학생 수가 맞는지 확인
# standard 가 가능한지 확인

# 4 4 3 0 0
# 3 3 3 2 0
# 2 2 3 2 2

# 보석 못 받아도 ok
# 학생은 항상 같은 색상의 보석만

# 질투심 : 가장 많은 보석을 가져간 학생의 보석 수
# 질투심 최소

