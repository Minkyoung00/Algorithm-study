#숫자카드 N개, 정수 M개

N = int(input()) #상근이가 가진 숫자 카드 개수
number = list(map(int, input().split())) #숫자 카드에 적혀있는 정수

number_set = set(number)


M = int(input())

find_num = list(map(int, input().split()))



ans = []
for num in find_num:
    if num in number_set:
        print(1, end=' ')
    else: 
        print(0, end=' ')
# print(' '.join(map(str, ans)))