#타일채우기3

N=int(input())
mod = 1000000007

#dp 테이블 초기화
#dp[i] = [i열 윗칸이 채워진 경우, i열의 아랫칸이 채워진 경우, i열이 전부 채워진 경우]
#bottom-up으로 ... 

dp = [[0,0,0] for _ in range(N+1)]
#초기화
dp[0] = [0,0,1]; dp[1] = [1,1,2]

for i in range(2,N+1):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % mod
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % mod
    dp[i][2] = (dp[i-1]*2 + dp[i-1][0] + dp[i-1][1] + dp[i-2][1]) % mod ##index error 해결해줘야함 i-2 

print(dp[N][2])