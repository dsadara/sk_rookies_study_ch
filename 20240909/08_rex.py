import re

data = """
123456-1234567
654321-7654321
"""

# 정규표현식 사용 안할 때

# formatted_text = []
# for element in data.strip().split("\n"):
#     words = element.split()
#     updated_words = []
#     for word in words:
#         # 주민등록번호 형식을 직접 확인하고 치환
#         if len(word) == 14 and word[6] == '-' and word[:6].isdigit() and word[7:].isdigit():
# 		        # 앞의 6자리와 하이픈을 그대로 두고 뒷자리 7개는 *로 치환
#             word = f"{word[:6]}-*******"  
#         updated_words.append(word)
#     formatted_text.append(" ".join(updated_words))
# output = "\n".join(formatted_text)
# print(output)

# 그룹은 괄호 ()를 사용하여 특정 부분을 묶어주는 것을 의미
pattern = re.compile(r"(\d{6})[-]\d{7}")

# \g<1>은 첫 번째 그룹에 매칭된 내용을 참조하는 방법
print(pattern.sub("\g<1>-*******", data))