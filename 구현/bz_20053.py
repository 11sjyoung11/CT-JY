#내 정답
n=int(input())
for i in range(n):
    k=int(input())
    arr=list(map(int,input().split()))
    m=max(arr)
    s=min(arr)
    print(s,m) #== print(min(arr),max(arr))