import zipfile
import os
import datetime
import ftplib
import time

dir_name = 'static'
current_date = datetime.datetime.now().strftime("%Y-%m-%d")

def zip_file(dir_name, current_date):
    with zipfile.ZipFile(f'{current_date}_{dir_name}.zip', 'w') as zipf:
        for dirpath, dirnames, filenames in os.walk(dir_name):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                zipf.write(file_path)

# 디렉토리 압축
zip_file(dir_name, current_date)

# 전송 전 대기
time.sleep(5)

# ftp 서버로 전송
ftp = ftplib.FTP("192.168.17.128")
ftp.login('msfadmin', 'msfadmin')
with open(rf"C:\python_ex\{current_date}_{dir_name}.zip", 'rb') as f:
    ftp.storbinary(rf"STOR {current_date}_{dir_name}.zip", f)
ftp.quit()