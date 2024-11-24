n = int(input())

dp=[1]*(n+1)

if n ==1:
    print(dp[1])
    
elif n==2:
    print(dp[2])
 

elif n >= 3:
    for i in range(3, n+1):
        dp[i]=dp[i-1]+dp[i-2]
    print(dp[n])