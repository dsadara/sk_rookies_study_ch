import ftplib

ftp = ftplib.FTP("192.168.17.128")
ftp.login('msfadmin', 'msfadmin')

with open(r"ftp_file.txt", 'wb') as f:
    ftp.retrbinary(r'RETR hello.txt', f.write)

ftp.quit()