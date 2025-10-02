m=int(input())

money=[500,100,50,10,5,1]
change=1000-m #1000-380=620
count=0
for i in money:
    count +=change//i #500원의 개수 1개 
    change %= i #500원 하고 나머지 120

print(count)