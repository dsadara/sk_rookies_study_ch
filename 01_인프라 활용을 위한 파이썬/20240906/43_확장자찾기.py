# 확장자가 .txt인 파일 찾기
import os

for dirpath, dirnames, filenames in os.walk(r"C:/python_ex"):
    print(f"Found directory: {dirpath}")
    for filename in filenames:
        if filename.endswith('.txt'):
            print(f"txt 파일 찾기: {filename}")
    print("-"*50)