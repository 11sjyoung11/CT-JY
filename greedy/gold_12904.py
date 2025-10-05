s=input()
t=list(map(str,input().split()))
#생각1 규칙1이 문자열의 뒤에 a를 추가하는거니까 aa,ba 만 나올 수 있음
#생각2 규칙2가 문자열의 뒤에 b를 추가하고 뒤집는거니까 ba,bb 만 나올 수 있음
# rul1=['BB','BA'] #b가 오면
# rul2=['BA','AA'] #a가 오면 
# if s == "B":
#     for i in range(len(t)):
#         if t[i::i+2] in rul1:
#             print("1")
#         else:
#             print("0")
# else:
#     for i in range(len(t)):
#         if t[i::i+2] in rul2:
#             print("1")
#         else:
#             print("0")
#틀린 이유: 저렇게 리스트를 넣어서 2개씩 판단하면 안된다....생각의 오류
#t의 길이가 s보다 길 때까지 규칙을 거꾸로 적용
#1. t의 마지막 글자가 A면 A를 뺀다
#2. t의 마지막 글자가 B면 B를 빼고 문자열을 뒤집는다.
#정답코드
S = list(map(str, input()))
T = list(map(str, input()))

while len(S) != len(T):
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T = T[::-1]

if S == T:
    print(1)
else:
    print(0)
    
#작은 것으로 큰것을 만들 때는 반대로 구하는 경우도 고려해보자