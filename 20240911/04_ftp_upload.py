import ftplib

ftp = ftplib.FTP("192.168.17.128")
ftp.login('msfadmin', 'msfadmin')

with open(r"C:\python_ex\example.txt", 'rb') as f:
    ftp.storbinary(r'STOR example.txt', f)

ftp.quit()