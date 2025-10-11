c = [list(map(int, input().split())) for _ in range(5)]  # 빙고판 숫자 5x5 입력
mc = []
for _ in range(5):
    mc += list(map(int, input().split()))  # 사회자가 부르는 숫자 25개 입력


def check():
    bingo = 0

    # 가로 확인
    for x in c: 
        if x.count(0) == 5:  # 한 줄이 모두 0이면 빙고
            bingo += 1

    # 세로 확인
    for i in range(5): 
        y = 0
        for j in range(5):
            if c[j][i] == 0:  # 세로 방향으로 0의 개수 세기
                y += 1
        if y == 5:  # 한 열이 모두 0이면 빙고
            bingo += 1

    # 왼쪽 위부터 시작하는 대각선 확인
    d1 = 0
    for i in range(5):
        if c[i][i] == 0:  # (0,0), (1,1), ... (4,4) 대각선
            d1 += 1
    if d1 == 5:  # 대각선이 모두 0이면 빙고
        bingo += 1

    # 오른쪽 위부터 시작하는 대각선 확인
    d2 = 0
    for i in range(5):
        if c[i][4-i] == 0:  # (0,4), (1,3), ... (4,0) 대각선
            d2 += 1
    if d2 == 5:  # 대각선이 모두 0이면 빙고
        bingo += 1

    return bingo  # 완성된 빙고 줄 개수 반환


cnt = 0  # 사회자가 부른 숫자 개수(빙고판에서 0으로 바꾼 개수)
for i in range(25):  # 사회자가 25개의 숫자를 하나씩 부름
    for x in range(5):
        for y in range(5):
            if mc[i] == c[x][y]:  # 부른 숫자가 빙고판에 있으면
                c[x][y] = 0       # 0으로 표시(지움)
                cnt += 1          # 숫자 부른 횟수 증가

    if cnt >= 12:  # 최소 12개 이상 불러야 빙고 3줄이 나올 수 있음
        result = check()  # 빙고 줄 개수 확인

        if result >= 3:   # 빙고가 3줄 이상이면
            print(i+1)    # 사회자가 몇 번째 숫자를 불렀을 때 빙고가 되는지 출력
            break         # 종료