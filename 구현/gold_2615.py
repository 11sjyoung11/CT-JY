omok = [list(map(int, input().split())) for _ in range(19)]  # 19x19 오목판 입력

# 방향: 오른쪽, 아래, 우하향, 우상향 (dx, dy)
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for i in range(19):  # 모든 행
    for j in range(19):  # 모든 열
        if omok[i][j] == 0:  # 바둑알이 없으면 건너뜀
            continue
        color = omok[i][j]  # 현재 바둑알 색(1:검은, 2:흰)
        for d in range(4):  # 4방향(가로, 세로, 우하향, 우상향) 검사
            cnt = 1  # 연속된 바둑알 개수
            x, y = i, j  # 현재 위치
            # 5개 연속 체크
            while True:
                nx = x + dx[d]  # 다음 위치 행
                ny = y + dy[d]  # 다음 위치 열
                # 범위 안이고, 같은 색이면
                if 0 <= nx < 19 and 0 <= ny < 19 and omok[nx][ny] == color:
                    cnt += 1  # 연속 개수 증가
                    x, y = nx, ny  # 위치 이동
                else:
                    break  # 연속이 아니면 종료
            # 5개 연속이고, 양쪽에 같은 색이 더 있으면 패스(6목 이상 금지)
            if cnt == 5:
                # 시작점 이전 위치
                px = i - dx[d]
                py = j - dy[d]
                # 끝점 다음 위치
                nx = x + dx[d]
                ny = y + dy[d]
                # 이전 위치에 같은 색이 있으면 6목이므로 패스
                if (0 <= px < 19 and 0 <= py < 19 and omok[px][py] == color):
                    continue
                # 다음 위치에 같은 색이 있으면 6목이므로 패스
                if (0 <= nx < 19 and 0 <= ny < 19 and omok[nx][ny] == color):
                    continue
                print(color)  # 이긴 색 출력
                print(i+1, j+1)  # 가장 왼쪽(또는 위) 바둑알 좌표 출력
                exit(0)  #  종료
print(0)  # 승부가 결정되지 않은 경우 0 출력




