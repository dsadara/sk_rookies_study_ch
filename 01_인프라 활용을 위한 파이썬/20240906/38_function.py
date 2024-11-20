def say_hello(name, greeting="안녕하세요"):
    greeting = f"{greeting} {name}님!"
    return greeting

result = say_hello("채현")
print(result)
print(say_hello("하윤", "반갑습니다."))