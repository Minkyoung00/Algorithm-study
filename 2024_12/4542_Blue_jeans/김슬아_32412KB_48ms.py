n = int(input())

def find_common_substring(strings):
    first_string = strings[0]
    max_common = ""
    
    # 첫 번째 문자열의 모든 부분 문자열 생성 (길이 3 이상)
    for length in range(3, len(first_string) + 1):  # 최소 길이 3부터 시작
        for start in range(len(first_string) - length + 1):
            substring = first_string[start:start + length]
            
            # 나머지 문자열에서 공통 여부 확인
            if all(substring in s for s in strings[1:]):
                # 최장 길이 또는 사전순으로 앞선 문자열 업데이트
                if len(substring) > len(max_common) or (len(substring) == len(max_common) and substring < max_common):
                    max_common = substring
    
    return max_common if max_common else "no significant commonalities"

for _ in range(n):
    m = int(input())
    strings = [input() for _ in range(m)]
    result = find_common_substring(strings)
    print(result)
