while True:
    arr=list(map(int,input().split()))
    k=arr[0]
    if k==0:
        break
    picksum=[]
    visited=[False]*(len(arr))
    def permutation(cnt,depth):
        if cnt==depth:
            print(*picksum)
        for index in range(1,len(arr)):
            if visited[index]==False:
                visited[index]=True
                picksum.append(arr[index])
                permutation(cnt+1,depth)
                # 백트래킹 하기 위해 되돌림
                picksum.pop()
                visited[index]=False
    permutation(0,6)
    print()
