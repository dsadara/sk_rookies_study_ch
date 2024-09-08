import os

# 탐색할 디렉터리 경로를 지정합니다.
search_dir = r"C:\python_ex"

# os.walk()로 디렉터리 구조 탐색
for dirpath, dirnames, filenames in os.walk(search_dir):
    for filename in filenames:
        # 파일의 절대 경로 생성
        full_path = os.path.join(dirpath, filename)
        print("Full path:", full_path)