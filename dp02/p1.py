T = int(input())
def f(N):
    if N==1:
        return 1
    if N==2:
        return 2
    elif N==3:
        return 4
    
    dp = [0]+[1,2,4]  
    for i in range(4, N + 1):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
    return dp[N] 


for _ in range(T):
    num = int(input())
    result = f(num)
    print(result%1000000009)

##################################################
#수정코드

T = int(input())

# 최대 N값을 미리 설정
MAX_N = 1000000
MOD = 1000000009

# 미리 dp 배열을 계산
dp = [0] * (MAX_N + 1)
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, MAX_N + 1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MOD

# 입력받은 테스트 케이스 처리
for _ in range(T):
    num = int(input())
    print(dp[num])
