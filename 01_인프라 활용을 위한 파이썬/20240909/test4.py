import os
import time
import re

file = 0
file_list = set()
num = 0
while num < 60:
    for dirpath,dirnames,filenames in os.walk(r"C:\python_ex\static"):
        a = len(filenames)
        files = set(filenames)
    if file != a:
        file = a
        result = files - file_list
        print(f"새로 추가된 파일: {result}")
        file_list = files
        for i in result:
            with open(f'C:\python_ex\static\{i}','r',encoding='utf-8') as reading:
                read = reading.read()
                pattern = re.compile(r"^[a-zA-Z0-9_.+-]+[@][a-zA-Z0-9-]+[.][a-zA-Z0-9.-]+$",re.MULTILINE)
                if pattern.match(read):
                    print(f"이메일이 감지되었습니다.\n감지된 이메일: {pattern.findall(read)}")
                pattern = re.compile(r"^//+",re.MULTILINE)
                if pattern.match(read):
                    print(f"주석이 감지되었습니다.\n감지된 주석: {pattern.findall(read)}")
                pattern = re.compile(r"^#+",re.MULTILINE)
                if pattern.match(read):
                    print(f"주석이 감지되었습니다.\n감지된 주석: {pattern.findall(read)}")
    time.sleep(5)
    num += 1