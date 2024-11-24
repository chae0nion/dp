N = int(input())

# N이 1 이하일 때 예외 처리
if N <= 0:
    print(0)
else:
    def fib(n):
        if dp[n] != 0:  # 이미 계산된 값이 있으면 반환
            return dp[n]

        # dp[n]이 0이라면, 점화식을 통해 계산
        dp[n] = fib(n - 3) + fib(n - 1)
        return dp[n]

    # dp 리스트 초기화 및 기저 사례만 미리 저장
    dp = [0] * (N + 1)
    dp[1] = 1
    if N >= 2:
        dp[2] = 1
    if N >= 3:
        dp[3] = 1

    print(fib(N))
