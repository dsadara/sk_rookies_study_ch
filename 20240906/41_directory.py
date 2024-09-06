import os

print(os.getcwd()+r'\33_tuple.py')

print(os.path.isfile("36_set.py"))
print(os.path.isfile(r"C:\python_ex\33_tuple.py"))

print(os.path.isdir(r"C:\python_ex"))

# 현재 디렉토리 리스트 출력
# print(os.listdir(r"../"))

entries = os.listdir('.')
# 폴더인지 확인 후 출력
for name in entries:
    if os.path.isdir(name):
        print(name)