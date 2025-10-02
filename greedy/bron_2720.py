k=int(input())
arr=[]
for i in range(k):
    arr.append(int(input()))
for n in arr:
    q,d,nikel,peny=25,10,5,1
    qa=n//q
    da=(n%q)//d
    ni=(n%q%d)//nikel
    pe=(n%q%d%nikel)//peny
    print(int(qa),int(da),int(ni),int(pe))

#1번째에 센트 단위를 정수로 두지 않아서 틀림
            