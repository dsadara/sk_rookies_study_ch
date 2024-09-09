import os

# 시스템 환경 변수에서 이메일 계정 정보 불러오기
send_email = os.getenv("SEND_EMAIL")
send_pwd = os.getenv("SEND_PWD")

print(f"Email: {send_email}, Password: {send_pwd}")