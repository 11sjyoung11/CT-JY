#1번째 시도
s=int(input())
cnt=0
while True:
    if s>=cnt:
        s-=cnt
        cnt+=1
    else:
        break
print(cnt,")")

#2번째 시도
s = int(input())
cnt = 1
ans = 0
while s >= cnt:
    s -= cnt
    ans += 1
    cnt += 1
print(ans)

        