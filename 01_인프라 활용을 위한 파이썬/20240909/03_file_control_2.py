import os, time

DIR_PATH = 'static'

pre_file = set(os.listdir(DIR_PATH))
# print(f"초기 파일: {pre_file}")

while True:
    current_file = set(os.listdir(DIR_PATH))
    # print(f"실시간 파일: {current_file}")

    # 차집합
    result_files = current_file - pre_file

    for result_file in result_files:
        print(f"새로운 탐지 파일: {result_file}")

    # 파일 업데이트
    pre_file = current_file

    time.sleep(5)