import sys
input = sys.stdin.read
data = input().split()
n, m = int(data[0]), int(data[1]) #n아이들의 수, 색상 수 M
jew = list(map(int, data[2:]))
#한명에게는 같은 색의 보석만 나누어줄수있음


    
start = 1
end = max(jew)

while start <= end:
    mid = (start + end) // 2
    kids = 0
    
    for j in jew:
        kids += (j+mid - 1) // mid
        
            
    if kids > n:
        start = mid + 1
        
    else:
        result = mid
        end = mid - 1
        
print(result)
    