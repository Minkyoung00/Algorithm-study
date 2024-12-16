# 블로그 참고 했습니다 ㅠ
import sys
input=sys.stdin.readline
N,B=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(N)]

# 행렬 곱셈 함수 
def matrix_mul(arr1,arr2):
    result = [[0]*N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            s= sum(arr1[row][i]*arr2[i][col] for i in range(N))
            result[row][col]=s%1000
    return result
#제곱 홀수 짝수 경우나누어
# 행렬 제곱 함수 구현
def power(n,arr):
    if n==1:
        return arr
    if n%2 ==0:
        half = power(n//2,arr)
        return matrix_mul(half,half)
    else:
        return matrix_mul(arr,power(n-1,arr))
    
for row in power(B,A):
    print(*[r%1000 for r in row])
