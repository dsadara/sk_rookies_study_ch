str = "Hello, Python!"

# 단순 추출 - Hello 문자만 출력하기
print(str[0] + str[1] + str[2] + str[3] + str[4])

# 슬라이싱 추출
print(str[0:5]) # 0 ~ 4 출력 하고 싶으면 5를 적어줘야 함

# 스텝
print(str[0:13:2]) # 2 -> 두칸씩 건너뛰기

#역순 슬라이싱

str = "Hello, Python!"
# 끝부터 시작까지, 한 칸씩 건너뛰며 역순으로 문자를 추출
print(str[::-1])
