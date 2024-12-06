n = int(input()) #잔의개수 1<=n<=10000
ml = [] #포도주 1000이하의 양
for _ in range(n): 
    ml.append(int(input()))
 #마신후원래 위치로, 연속으로 3잔 불가능
dp =[0]*n
#최대한 많은 양 맛보기

if n > 1:
    dp[1] = ml[0] + ml[1]
    
if n > 2:
    dp[2] = max(ml[2]+ ml[1], ml[2]+ml[0], dp[1])
    
for i in range(3,n):
    dp[i] = max(dp[i-1], dp[i-3]+ml[i-1]+ml[i], dp[i-2]+ml[i] )
print(dp[n-1])
    