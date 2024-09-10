import os, time
import re

DIR_PATH = 'static'
email_pattern = re.compile(r"[a-zA-Z0-9_.+-]+[@][a-zA-Z0-9-]+[.][a-zA-Z0-9.-]+")

pre_file = set(os.listdir(DIR_PATH))
#print(f"초기 파일: {pre_file}")

while True:
    current_file = set(os.listdir(DIR_PATH))
    #print(f"실시간 파일: {current_file}")
    
    # 차집합
    result_files = current_file - pre_file
    
    for result_file in result_files:
        print(f"새로운 탐지 파일: {result_file}")
        file_path = os.path.join(os.getcwd(), DIR_PATH, result_file)
        # print(file_path)
        with open(file_path, 'r', encoding='utf-8') as file:
            # print(file.read())
            lines_list = file.readlines()
            for num, value in enumerate(lines_list):
                # print(f"줄 번호 : {num+1}, 값 : {value}", end="")
                if value.startswith(("#", "//")):
                    print(f"{num+1} 라인, 주석 탐지  : {value}")
                elif email_pattern.search(value):
                    print(f"{num+1} 라인, 이메일 주소 탐지 : {value}")
    
    # 파일 업데이트
    pre_file = current_file
    
    time.sleep(5)