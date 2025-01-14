n = int(input())
x = list(map(int, input().split()))
#좌표를 정렬하고, 정렬된 좌표에 순서를 맵핑함

#배열을 정렬하여 순서를 찾기
sorted_x = sorted(set(x))


#원래 숫자에 위치에 맞는 압축된 값을 배치치
dic = {sorted_x[i] : i for i in range(len(sorted_x))}


for i in x:
    print(dic[i], end = ' ')