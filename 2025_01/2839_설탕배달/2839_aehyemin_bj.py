n = int(input())
#5키로, 3킬로 
#혼합해서 구했을때랑, 한개로 구했을때 min

result = -1

for five in range(n // 5, -1, -1):
    remain = n - (5*five)
    if remain % 3 == 0:
        three = remain // 3
        result = five + three
        break
print(result)