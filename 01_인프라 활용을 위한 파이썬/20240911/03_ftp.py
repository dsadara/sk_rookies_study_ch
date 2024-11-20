import ftplib

ftp = ftplib.FTP("192.168.17.128")

ftp.login('msfadmin', 'msfadmin')

ftp.retrlines('LIST')

print(ftp.nlst())

ftp.quit()