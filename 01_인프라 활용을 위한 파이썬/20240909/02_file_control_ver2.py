import os
def count_files_and_directories(dir):
    # 파일 및 디렉터리 개수 계산
    total_dir = 0
    total_file = 0
    
    for dirpath, dirnames, filenames in os.walk(dir):
        for dirname in dirnames:
            # 이런식으로 확장자 검사
            if dirname == '20240909':
                print("20240909 접근")
            total_dir = total_dir + 1
        for filename in filenames:
            total_file += 1

    return total_dir, total_file

directory = input("디렉토리 경로 입력: ")
total_dir, total_file = count_files_and_directories(directory)

print(f"서브 디렉터리 개수: {total_dir}")
print(f"서브 파일 개수: {total_file}")