import sys
input = sys.stdin.readline

N=int(input())

arr = list(map(int,input().split()))

dp = [1]*N 
 # [1,1,1,1,1]=>[1,2,1,1,1]=>[] 10,20,20,30,40
for i in range(1,N):
    for j in range(i):
        if arr[i]>arr[j]: 
            dp[i]= max(dp[i],dp[j]+1)
print(arr)
print(max(dp))