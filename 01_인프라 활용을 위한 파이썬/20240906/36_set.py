my_set = {1, 2, 3, 4 ,5}
my_set.add(6)
print(my_set)
my_set.remove(1)
print(my_set)

# 순서 없기 떄문에 인덱스 참조 불가능
# myset[0]

# 합칩합

A = {1, 2, 3}
B = {3, 4, 5}

result_union = A | B
print(result_union)  # {1, 2, 3, 4, 5}

