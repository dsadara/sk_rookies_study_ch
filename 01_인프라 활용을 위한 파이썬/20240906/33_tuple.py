my_tuple = (1, 2, 3)

# 튜플은 할당 안됨
# my_tuple[0] = 4

# 튜플 안에 리스트에는 할당 가능

mixed_tuple = (1, "apple", [2, 4, 6])
print("Original Tuple:", mixed_tuple)

mixed_tuple[2][1] = 5
print("Modified Tuple:", mixed_tuple)

# 튜플 리스트로 변환

my_tuple = (1,2,3)
print(my_tuple)
my_list=list(my_tuple)
print(my_list)