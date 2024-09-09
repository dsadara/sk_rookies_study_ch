import re

# 원시 문자열을 사용하여 모음 찾는 패턴을 컴파일하고 대소문자를 구분하지 않는 옵션 설정
pattern = re.compile(r'[aeiou]', flags=re.I)

text = "Hello World"

# 컴파일된 패턴 객체를 사용하여 findall() 메서드 실행
matches = pattern.findall(text)
print(matches)  # ['e', 'o', 'o']