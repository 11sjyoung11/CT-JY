# 스위치 개수
n = int(input())
# 스위치 상태
switches = list(map(int, input().split()))

student_count = int(input())

for _ in range(student_count):
    gender, number = map(int, input().split())

    if gender == 1:
        for i in range(number - 1, n, number):
            switches[i] = 1 - switches[i]

    else:
        idx = number - 1
        left = idx - 1
        right = idx + 1

        switches[idx] = 1 - switches[idx]

        while left >= 0 and right < n and switches[left] == switches[right]:
            switches[left] = 1 - switches[left]
            switches[right] = 1 - switches[right]
            left -= 1
            right += 1

for i in range(n):
    print(switches[i], end=' ')
    if (i + 1) % 20 == 0:
        print()