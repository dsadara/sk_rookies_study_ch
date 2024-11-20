import os, time, re

def check_email(filepath):
    pattern = re.compile(r"[\w_.+-]+@[\w-]+[.][\w.-]+")
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line, content in enumerate(lines):
            if pattern.search(content):
                print(f"[이메일발견][line:{line}]{content}", end="")

def check_annotation(filepath):
    pattern = re.compile(r"^[#//]", re.MULTILINE)
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line, content in enumerate(lines):
            if pattern.match(content):
                print(f"[주석발견][line:{line}]{content}", end="")

# 모니터링할 디렉토리 경로 설정
DIR_PATH = 'static'
file_set_before = set(os.listdir(DIR_PATH))

while True:
    file_set_new = set(os.listdir(DIR_PATH))
    update = set.difference(file_set_new, file_set_before)
    for file in update:
        file_path = os.path.join(DIR_PATH, file)
        print(f"새로 생성된 파일:{file}")
        check_email(file_path)
        check_annotation(file_path)
        print()
    file_set_before = file_set_new
    time.sleep(1)