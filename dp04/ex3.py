# maximum subarray; 연속한 항들로 이루어진 부분 배열 선택 시, 그 합이 최대가 되도록 하는 것
# 음수의 처리가 까다로움
# dp[i]= Xi를 오른쪽 끝으로 하는 연속 부부 배열의 합의 최대값
# 점화식: 합이 양수가 되면 유직하고 음수가 되면 버리는 것(0+Xi)
import sys
input=sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))


# 음수만 있는 경우 A = [-1,-2,-3] , dp = [0,0,0]이 출력됨(정답:-1)
if max(A) <= 0: 
    print(max(A))

else:
    dp = [0]*n
    dp[0] = max(0,A[0]) #음수 => 0, 양수면 A[0] 

    #점화식
    for i in range(1,n):
        dp[i] = max(dp[i-1]+A[i], 0) #A index가 n-1까지밖에 없음, index error 주의
        
# dp[i] = A[i] 를 오른쪽 끝으로 하는 연속합의 최대값

print(max(dp))

