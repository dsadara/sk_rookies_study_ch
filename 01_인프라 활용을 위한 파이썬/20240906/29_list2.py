list = [1,2,3,4, "test", 5]

list.append(6)
print(list)

# 2번 인덱스에 10 넣기
list.insert(2, 10)
print(list)

# 해당 값을 제거해줌
list.remove("test")
print(list)

# 인덱스에 있는 값을 삭제
del list[1]
print(list)