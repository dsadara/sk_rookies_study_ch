import zipfile
import os
import ftplib
import datetime
import time

def zip_file(folder_path, zip_path):
    # ZIP 파일 생성
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                zipf.write(file_path)

# 사용 예
current_day = datetime.datetime.now().strftime("%Y-%m-%d")
zip_file('static', f'static_{current_day}.zip')

def upload_file(ftp, filename):
    with open(filename, 'rb') as f:
        ftp.storbinary('STOR ' + filename, f)   # f는 압축한 파일 이름

time.sleep(5)
ftp = ftplib.FTP("192.168.56.103")
ftp.login('kali','kali')
upload_file(ftp, f'static_{current_day}.zip')
ftp.quit()