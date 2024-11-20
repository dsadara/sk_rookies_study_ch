import re

text = "오늘은 2024년 9월 9일입니다."

pattern = re.compile(r'\d+') # \d 숫자 + 1개이상

matches = pattern.findall(text)

print(matches)