result = 0 
max_value = 0
min_value = 0
first_input = True

while True:
    num = int(input("숫자를 입력하세요: "))
    if num == 0:
        break
    result = result + num

    if first_input:
        max_value = num
        min_value = num
        first_input = False
    elif num > max_value:
        max_value = num
    elif num < min_value:
        min_value = num

print(f"최종 합계: {result}")
print(f"최댓값 합계: {max_value}")
print(f"최솟값 합계: {min_value}")