n = int(input())
k = []  # 빈 리스트 선언
for _ in range(n):
    k.append(int(input()))  # 입력 값 추가

def f(num):
    dp = [[0, 0] for _ in range(num + 1)]

    if num==0:
        dp[0]=[1,0] 

    if num ==1:
        dp[1] = [0, 1]  

    if num >= 2:
        dp[0]=[1,0]
        dp[1]=[0,1]
        for i in range(2, num + 1):
            dp[i][0] = dp[i-1][0] + dp[i-2][0]
            dp[i][1] = dp[i-1][1] + dp[i-2][1]

    return dp[num]

# 결과 출력
for num in k:
    result = f(num)
    print(result[0], result[1])
