from sys import stdin
from collections import deque

N, M, R = map(int, stdin.readline().split())  # 행, 열, 회전 횟수 입력

matrix = []
answer = [[0]*M for _ in range(N)]  # 회전 결과를 저장할 배열
deq = deque()  # 테두리 원소를 담을 덱

for i in range(N):
    matrix.append(list(stdin.readline().split()))  # 행렬 입력

loops = min(N, M) // 2  # 테두리(겹)의 개수 계산 , 5*3 행렬이면 1개, 6*4 행렬이면 2개
for i in range(loops):
    deq.clear()  # 덱 초기화

    # 위쪽 테두리 원소 덱에 추가
    deq.extend(matrix[i][i:M-i])
    # 오른쪽 테두리 원소 덱에 추가
    deq.extend([row[M-i-1] for row in matrix[i+1:N-i-1]])
    # 아래쪽 테두리 원소 덱에 추가 (역순)
    deq.extend(matrix[N-i-1][i:M-i][::-1])
    # 왼쪽 테두리 원소 덱에 추가 (역순)
    deq.extend([row[i] for row in matrix[i+1:N-i-1]][::-1])
    
    deq.rotate(-R)  # 덱을 R번 반시계 방향으로 회전
    
    # 회전된 덱에서 값을 꺼내서 결과 배열에 채움
    for j in range(i, M-i):                 # 위쪽
        answer[i][j] = deq.popleft()
    for j in range(i+1, N-i-1):             # 오른쪽
        answer[j][M-i-1] = deq.popleft()
    for j in range(M-i-1, i-1, -1):         # 아래쪽
        answer[N-i-1][j] = deq.popleft()  
    for j in range(N-i-2, i, -1):           # 왼쪽
        answer[j][i] = deq.popleft()    

for line in answer:
    print(" ".join(line))  # 회전 결과 출력