#1
name=input("이름: ")
domain=input("도메인: ")
print(f"{name}@{domain}.com")
# email = name + "@" + domain + ".com"

#2

sentence1=input("문장1: ")
sentence2=input("문장2: ")
sentence3=input("문장3: ") + "."

# sentences = [sentence1, sentence2, sentence3]

result=". ".join([sentence1, sentence2, sentence3])
print(result)

#3

word=input("반복할 문자열을 입력하세요:")
times=int(input("반복 횟수를 입력하세요:"))
result = word * times
print(result)