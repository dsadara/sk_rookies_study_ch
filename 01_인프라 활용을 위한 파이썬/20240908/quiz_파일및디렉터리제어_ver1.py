'''
2) 선택 과제 - 파일 및 디렉터리 제어
 - 1) 전체 디렉터리 트리 탐색 및 파일과 디렉터리 개수 계산
 - 2) 디렉토리 파일 모니터링 시스템 구현 - 단계 1
'''

import os

def count_files_and_directories(path):

    file_count = 0
    dir_count = 0

    for dirpath, dirnames, filenames in os.walk(path):
            entries = os.listdir(dirpath)
            for name in entries:
                if os.path.isfile(name):
                    file_count += 1
                    print(name)
                elif os.path.isdir(name):
                    dir_count += 1
                    print(name)

    return file_count, dir_count

curr_path = os.getcwd()
result = count_files_and_directories(curr_path)

print(f"전체 파일의 개수:{result[0]}")
print(f"전체 서브디렉터리의 개수:{result[1]}")
