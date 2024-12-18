k = int(input())
num = []
for _ in range(k):
    value = int(input())
    if value != 0 :
        num.append(value)
    else:
        num.pop()
if num:
    print(sum(num))
else: 
    print(0)