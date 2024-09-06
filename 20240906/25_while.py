count = 0
while count < 5:
    print("현재 카운트:", count)
    count += 1  # count를 1씩 증가시켜 조건이 거짓이 됩니다.

# 무한루프에 탈출조건주기
while True:
    user_input = input("종료하려면 exit 입력: ")
    print(f"입력한 데이터: {user_input}")
    if user_input == 'exit':
        break

# reverse string

user_input = input("문자열을 입력하세요: ")
reversed_string = ""
index = len(user_input) - 1

while index >= 0:
    reversed_string = reversed_string + user_input[index]
    index = index - 1

print("거꾸로 된 문자열:", reversed_string)