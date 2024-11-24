#top down 문제 해결 방식/ 재귀 사용

N = int(input())
mod = 100000

def DFS(n, L, A):
    # n: n일차, L: 남은 지각횟수, A: 남은 결석횟수
    # earyl return
    if L == 0 or A == 0: return 0
    if n == 0: return 1

    #memorization(load)
    if DP[n][L][A]: return DP[n][L][A]

    #subproblems
    ret = (DFS(n-1,L, 3) + DFS(n-1, L-1, 3) + DFS(n-1, L, A-1)) % mod
        # n일차 출석 , n일차 지각, n일차 결석

    #memorization(save)
    DP[n][L][A] = ret

    return ret

DP = [[[0]*4 for _ in range(3)] for _ in range(N+1)]


print(DFS(N, 2, 3))