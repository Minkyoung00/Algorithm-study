N, K = map(int, input().split())
num = [int(i) for i in input()]
result = []  

remove_count = K  

for i in range(N):
    while remove_count > 0 and result and result[-1] < num[i]:
        result.pop()
        remove_count -= 1
    
    result.append(num[i])

print(''.join(map(str, result[:N-K])))