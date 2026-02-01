password = "python1234"
while True:
    pwd = input("Enter the password: ")
    if pwd == password:
        print("Access granted.")
        break
print("로그인 성공")