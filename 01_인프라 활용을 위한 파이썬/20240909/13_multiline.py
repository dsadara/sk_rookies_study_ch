import re

# 테스트할 문자열 정의
text = """
Hello World!
Welcome to the universe.
Number: 100, Email: hello@example.com
Patterns are everywhere. They help us solve problems and organize our lives.
Look into the woods and you'll find many oooooohs and aaaaaahs.
"""

# '^' 메타 문자: 문자열의 시작과 일치 (멀티라인 모드 사용)
# 멀티라인 모드 : 여러 줄로 구성된 경우 각 줄의 시작(^)과 끝($)에 해당하는 부분을 정확히 판별하기 위해 필요
pattern_caret = re.compile(r'^Hello', re.MULTILINE)
matches_caret = pattern_caret.findall(text)
print('^ 메타 문자:', matches_caret)  # ['Hello']

# '$' 메타 문자: 문자열의 끝과 일치 (멀티라인 모드 사용)
pattern_dollar = re.compile(r'com$', re.MULTILINE)
matches_dollar = pattern_dollar.findall(text)
print('$ 메타 문자:', matches_dollar)  # ['com']

# '?' 메타 문자: 바로 앞의 문자가 0번 또는 1번 나타나는 경우
# Wrld World는 됨  Wooooooorld는 안됨
pattern_question = re.compile(r'Wo?rld')
matches_question = pattern_question.findall(text)
print('? 메타 문자:', matches_question)  # ['World']

# '{n}' 메타 문자: 바로 앞의 문자가 정확히 n번 반복될 때
pattern_exact = re.compile(r'o{2}')
matches_exact = pattern_exact.findall(text)
print('{n} 메타 문자:', matches_exact)  # ['oo']

# '{n,}' 메타 문자: 바로 앞의 문자가 n번 이상 반복될 때
pattern_at_least = re.compile(r'o{2,}')
matches_at_least = pattern_at_least.findall(text)
print('{n,} 메타 문자:', matches_at_least)  # ['oo', 'oo']

# '{n,m}' 메타 문자: 바로 앞의 문자가 최소 n번, 최대 m번 반복될 때
pattern_range = re.compile(r'o{1,2}')
matches_range = pattern_range.findall(text)
print('{n,m} 메타 문자:', matches_range)  # ['oo', 'o', 'oo']