import os

search_dir = r"C:\python_ex"

# os.walk()로 디렉터리 구조 탐색
for dirpath, dirnames, filenames in os.walk(search_dir):
    # 현재 탐색중인 디렉토리 경로 출력
    print(f"FOUND DIRECTORY: {dirpath}")

    # 현재 디렉터리 안에 있는 서브디렉터리 목록 출력
    print(f"SUbdir: {dirnames}")

    # 현재 디렉터리 안에 있는 파일 목록 출력
    print(f"File: {filenames}")

    # 가독성을 위한 구분선
    print("-"*50)