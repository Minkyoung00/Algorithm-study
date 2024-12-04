# 입력값 받기
N = int(input())  # 첫 번째 입력값 (갯수)
numbers = set(map(int, input().split()))  

M = int(input())  # 두 번째 입력값 (갯수)
numbers2 = list(map(int, input().split()))  

# numbers2에 있는 각 값이 numbers에 있는지 확인
for i in numbers2:
    if i in numbers:
        print("1", end=' ')  # 있으면 1 출력
    else:
        print("0", end=' ')  # 없으면 0 출력
