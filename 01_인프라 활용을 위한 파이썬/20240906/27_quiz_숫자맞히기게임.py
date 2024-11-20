import random

# 1과 100 사이 랜덤 정수
computer_number = random.randint(1, 100)

attempt = 0
while True:
    user_number = int(input("1부터 100 사이의 임의의 숫자를 입력하세요:"))
    attempt += 1
    if user_number > computer_number:
        print(f"정답은 더 높은 숫자입니다. (입력횟수:{attempt})")
    elif user_number < computer_number:
        print(f"정답은 더 낮은 숫자입니다. (입력횟수:{attempt})")
    elif user_number == computer_number:
        print(f"정답입니다! {attempt}번 만에 맞추셨습니다.")
        break

# 0과 1사이 실수
# number = random.random()
# # print(number)

