import re

text = "abc def"
pattern = re.compile(r'a.') # a 다음에 어떤 문자든 일치

match = pattern.search(text)
if match:
    print(match.group())  # 'ab' 출력 -> 검색 결과만 보기
else:
    print("No match found")