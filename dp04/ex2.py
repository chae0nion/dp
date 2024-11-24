#거스름돈 만들기 문제 => 그리디 실패함(가장 큰 동전부터 사용)
#동전의 최소개수 구하는 문제: 부분문제 => 총 가치가 i가 될 때 필요한 동전의 최소개수
# //마지막 어떤 동전을 썼는지에 따라 분류
# (W-마지막동전가치) + 1

#가치합이 w가 되는 방법수 구하기: 순서가 중요하지 않을 경우 => 조합의 수로 바꾸기
# //가장 작은 동전부터 사용할 때부터 모든 조합을 dp에 기록..한다는데 잘 모르겠므

#n가지 동전, 가치의 합=k원, 가치가 같은 동전 허용
#출력: 사용한 동전의 최소 개수/ 불가능한 경우 -1
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coin = []
max = int(1e10)

for _ in range(n):
    coin.append(int(input()))

coin = list(set(coin)) #중복처리(집합)=> 다시 list로
#dp[i] = i원의 가치를 만들기 위해 사용한 동전의 최소 개수
dp = [max] * (100001) #index error 방지, 동전의 가치가 10만 아래인데 k는 만까지 밖에 안됨.
for c in coin:
    dp[c]=1

#점화식
for i in range(1,k+1):
    for c in coin:
        if i <= c: continue
        dp[i] = min(dp[i], dp[i-c]+1)

print(dp[k] if dp[k] != max else -1)