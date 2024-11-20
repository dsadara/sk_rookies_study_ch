person = {
    "name":"taeyeong",
    "age":20,
    "city":"Seoul"
}

print(person["name"])
print(person["city"])

# 존재하지 않는 키를 가져올 때 에러 발생 안시키고 NONE 반환
print(person.get("game", "존재하지 않는 키입니다."))

# 요소제거

print(person.pop("name"))
print(person)
print(person.popitem)
print(person)

# 요소 접근

print(person.keys())
for i in person.keys():
    print(i)

print(person.items())
for key, value in person.items():
    print(f"key: {key}, value: {value}")