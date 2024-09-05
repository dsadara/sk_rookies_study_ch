# 방법 1 % 연산자
name = "임채현"
target = "파이썬 자동화"

print("내 이름은 %s입니다 %s 학습" % (name, target))



# 방법 2 format() 메소드
# 파이썬 2.6

name = "김태영"
age = 20

print("내 이름은 {}이고 나이는 {}살 입니다.".format(name,age))


# 방법 3 문자열 리터럴 f-string
# 파이썬 3.6 가장 최신 방법

print(f"내 이름은 {name}이고 나이는 {age + 10}살 입니다.")