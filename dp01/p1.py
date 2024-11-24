n = int(input())

s=[0]*(n+1)

if n==1:
    s[1]=1

if n==2:
    s[1]=1
    s[2]=3

if n>=3:
    s[1]=1
    s[2]=3
    for i in range(3,n+1):
        s[i]=s[i-1]+ 2*s[i-2] #1씩 더하는 게 아님..가지수인데 그걸 착각

result = s[n] % 10007

print(result)
