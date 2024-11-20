# 리스트는 다른 자료형 넣기 가능
list = [1,'test',3,4,5]

# 리스트 슬라이싱
result = list[1:4] # 4-1

print(result)

# 리스트 수정
list[1] = 2
print(list)

# 리스트 결합

list2 = ["a", "b", "c"]

list3 = list + list2
print(list3)

