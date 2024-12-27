import sys
N,K=map(int,input().split())
num_str=input()
stack=[]

to_remove=K

for num in num_str:
    while to_remove>0 and stack and stack[-1]<num:
        stack.pop()
        to_remove-=1
    stack.append(num)

# 모든 숫자가 내림차순일 때 to_remove가 전혀 깎이지 않은 경우도 있으므로
stack=stack[:N-K]

print(*stack,sep="")
