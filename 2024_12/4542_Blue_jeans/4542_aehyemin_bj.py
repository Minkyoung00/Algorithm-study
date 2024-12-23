n = int(input())
for i in range(n):
    m = int(input())
    dna = [input().strip() for _ in range(m)]
    
    fir = dna[0]
    ans = None
    
    for j in range(60, 2, -1):
        sub = set(fir[k:k+j] for k in range(61 - j))
        
        sub_sort = sorted(sub)
        
        found = False
        
        for sub in sub_sort:
            if all(sub in seq for seq in dna):
                ans = sub
                found = True
                break
            
        if found:
            break
        
    #최소 길이 3이상의 공통 부분 문자열
    
    
    if ans and len(ans) >= 3:
        print(ans)
    else: 
        print("no significant commonalities")