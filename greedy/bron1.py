T = int(input())

if T % 10 != 0:
    print(-1)
else:
    Acount = T // 300
    Bcount = T % 300 // 60
    Ccount = T % 300 % 60 // 10

    print(Acount, Bcount, Ccount)