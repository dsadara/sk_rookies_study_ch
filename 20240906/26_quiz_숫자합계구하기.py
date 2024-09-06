sum = 0
while True:
    number = int(input("숫자를 입력하세요: "))
    sum += number
    if number == 0:
        break

print(f"합계는 {sum}입니다.")