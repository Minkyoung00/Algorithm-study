k = int(input())
sign = list(input().split())
visited = [False] * 10
min_ans = ''
max_ans = ''

def check(i,j,k):
    if k == "<":
        return i < j
    else:
        return i > j
    
def solu(idx, num):
    global min_ans, max_ans
    
    if idx == k+1:
        if len(min_ans) == 0 :
            min_ans = num
        else :
            max_ans = num
        return
    
    for i in range(10):
        if not visited[i]:
            if idx == 0 or check(int(num[-1]), i, sign[idx -1]):
                visited[i] = True
                solu(idx +1, num + str(i))
                visited[i] = False
      
solu(0, '') 
print(max_ans)
print(min_ans)