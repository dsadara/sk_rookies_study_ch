import re

phone_num = input("전화번호를 입력하세요 (000-0000-0000):")

pattern = re.compile(r'^\d{3}-\d{4}-\d{4}$')    # ^ $ -> 시작과 끝 체크

match = pattern.search(phone_num)

if match:
    print("올바른 전화번호")
else:
    print("잘못된 전화번호")
