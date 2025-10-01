k=int(input())
arr=[]
for i in range(k):
    arr.append(int(input()))
for n in arr:
    q,d,nikel,peny=0.25,0.1,0.05,0.01
    qa=n//q
    da=(n%q)//d
    ni=(n%q%d)//nikel
    pe=(n%q%d%nikel)//peny
    print(int(qa),"+",int(da),"+",int(ni),"+",int(pe))

            