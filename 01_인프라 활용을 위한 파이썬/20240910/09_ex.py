import requests

API_KEY = "---"
url = f"https://openexchangerates.org/api/latest.json?app_id={API_KEY}"

response = requests.get(url)
rates = response.json()['rates'] # 딕셔너리

from_currency = input("변환할 통화(예: USD): ")
to_currency = input("목표 통화(예: EUR): ")
amount = float(input("금액 입력: "))

# 환율 변환 계산식
base_amount = amount / rates[from_currency]
result_amount = base_amount * rates[to_currency]

print(result_amount)