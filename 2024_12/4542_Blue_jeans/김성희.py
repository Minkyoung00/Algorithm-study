import sys
input = sys.stdin.readline

def LCS(source, compare):
    length = len(compare)
    matrix = [[0]*(61) for _ in range(length+1)]
    max_len = 0
    seq = []
    
    for i in range(1, length+1):
        for j in range(1, 61):
            if source[j-1] == compare[i-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
                if matrix[i][j] > max_len:
                    max_len = matrix[i][j]
    
    # 모든 부분에 대해 최대 길이만큼 검색
    for i in range(1, length+1):
        for j in range(1, 61):
            if matrix[i][j] == max_len:
                substring = source[j-max_len:j]
                if len(substring) >= 3 and substring not in seq:
                    seq.append(substring)
    
    return seq

def check(base):
    # 첫 번째 문자열에서 찾은 부분 문자열들
    first_lcs = LCS(base[0], base[1])
    
    if not first_lcs:
        return "no significant commonalities"
    
    # 모든 문자열에 공통으로 포함되는지 확인
    for lcs in first_lcs:
        if all(lcs in b for b in base[2:]):
            return lcs
    
    return "no significant commonalities"

total = int(input())
for _ in range(total):
    m = int(input())
    base = [input().strip() for _ in range(m)]
    
    print(check(base))
