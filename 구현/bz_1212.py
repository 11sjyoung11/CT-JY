
## 1.  답은 맞지만 시간 초관
num = list(map(int, input().split()))  # 8진수 입력
arr = []

for i in range(len(num)):
    n = num[i]
    bin_str = ''  # 각 숫자를 2진수로 저장할 문자열

    while n > 0:           # 8진수를 2진수로 직접 변환
        s = n % 2          # 2로 나눈 나머지 (0 또는 1)
        arr.append(s)      # 결과 배열에 추가 
        n //= 2            # n을 2로 나눔
    
    arr.reverse()          # 출력 순서를 맞추기 위해 뒤집음
    for j in range(len(arr)):
        print(arr[j], end='')
    print()
    arr.clear()            # 다음 숫자를 위해 초기화

## 2. bin 함수는 10진수만 받으므로 8진수를 10진수로 바꾼 후 2진수로 변환
print(bin(int(input(), 8))[2:])
#input() : 입력을 문자열로 받음 (예: '314')
#int(input(), 8) : 입력받은 문자열을 8진수로 해석해서 10진수로 변환
#bin(...)[2:] : 10진수를 2진수 문자열로 변환하고, 앞의 '0b'를 제외함
#print(...) : 최종적으로 2진수 문자열을 출력

#3. 
num = input().strip()
result = ''
for i, digit in enumerate(num):
    b = bin(int(digit))[2:].zfill(3)
    if i == 0:
        b = str(int(b))
    result += b
print(result)