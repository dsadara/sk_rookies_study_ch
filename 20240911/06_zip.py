import zipfile

with zipfile.ZipFile('output.zip', 'w') as zipf:
    zipf.write(r"C:\python_ex\hello.txt")
    zipf.write(r"C:\python_ex\ftp_file.txt")