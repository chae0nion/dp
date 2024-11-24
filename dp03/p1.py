import sys
input = sys.stdin.readline

# DFS(what, here): here번째 가게에서 what을 마실 차례일 때 마실 수 있는 최대값
def DFS(here, what):
    # Early Return
    if here == N: return 0
    if what > 2: return DFS(here, what-3)

    # Memoization(Load)
    if DP[here][what] != -1: return DP[here][what]

    # Subproblems
    if milk[here] == what: 
        ret = max(DFS(here+1, what), DFS(here+1, what+1) + 1)
    else:
        ret = DFS(here+1, what)
    
    # Memoizatin(Save)
    DP[here][what] = ret

    return ret

N = int(input())
milk = list(map(int, input().split()))

DP = [[-1]*3 for _ in range(N)]

print(DFS(0, 0))
