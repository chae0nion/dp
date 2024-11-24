#bottom up

N = int(input())

A = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(N)] 
# A[0]에 [0, 0, 0]을 넣고, A[1]부터 N까지 데이터를 저장

# dp 테이블 초기화
dp = [[0, 0, 0] for _ in range(N + 1)]
dp[1] = [A[1][0], A[1][1], A[1][2]]  # 첫 번째 집 초기화

# 점화식
for n in range(2, N + 1):
    dp[n][0] = min(dp[n - 1][1], dp[n - 1][2]) + A[n][0]  # n번 집 빨강
    dp[n][1] = min(dp[n - 1][0], dp[n - 1][2]) + A[n][1]  # n번 집 초록
    dp[n][2] = min(dp[n - 1][0], dp[n - 1][1]) + A[n][2]  # n번 집 파랑

# 결과 출력
print(min(dp[N]))
