import re

phone_number = '000-0000-0000'
phone_number = input(f"전화번호를 입력하세요 ({phone_number}):")

pattern = re.compile(r'^(\d{3})-(\d{4})-(\d{4})$')

match = pattern.search(phone_number)
if match:
    print("올바른 전화번호 형식입니다.")
else:
    print("잘못된 전화번호 형식입니다.")