import re

text = "aac"
pattern = re.compile(r'ab*c') # b가 없어도 되고 있어도 되는거 모든거 찾음
matches = pattern.findall(text)
print(matches)  # ['ac']