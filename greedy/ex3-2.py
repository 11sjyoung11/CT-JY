#큰 수의 법칙
n,m,k=map(int,input().split(()))
#n개의 수를 공백으로 구분하여 입력받기
data=list(map(int,input().split(())))
data.sort() #입력받은 수 정렬하기
first=data[n-1] #가장 큰 수
second=data[n-2] #두번째로 큰 수

count = int(m/(k+1))*k #가장 큰 수가 더해지는 횟수
count += m%(k+1) #나머지 횟수 더하기

result=0
result+=count*first #가장 큰 수 더하기
result+=(m-count)*second #두번째로 큰 수 더하기

print(result)