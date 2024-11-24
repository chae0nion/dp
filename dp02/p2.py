n = int(input())

wine= [0]+[]
for _ in range(n):
    wine.append(int(input()))

dp=[0]*(n+1)

dp[0]=0
if n==1:
    dp[1]= wine[1]
if n==2:
    dp[2]= wine[1]+wine[2]

if n >=3:
    for i in range(3,n+1):
         dp[i] = max(wine[i]+wine[i-1]+dp[i-3], wine[i]+dp[i-2],dp[i-1])

print(dp[n])