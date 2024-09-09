import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# 발신자, 수신자 및 SMTP 서버 정보 설정
send_email = "fkelfkenl10@naver.com"
send_pwd = "Lch885233@"
recv_email = "lim971230@gmail.com"

# SMTP 서버 주소와 포트
smtp_name = "smtp.naver.com"
smtp_port = 587

# MIMEMultipart 객체 생성: 이메일 본문과 첨부 파일을 포함할 수 있음
msg = MIMEMultipart()
msg['Subject'] = "첨부 파일 포함된 이메일 테스트"
msg['From'] = send_email
msg['To'] = recv_email

# 이메일 본문 내용
text = "첨부 파일이 포함된 이메일입니다.\n텍스트1\n텍스트2"
email_body_part = MIMEText(text, 'plain', 'utf-8')
msg.attach(email_body_part)

# 첨부 파일 경로
file_path = r"C:\python_ex\example.txt"

with open(file_path, 'rb') as file:
    file_part = MIMEApplication(file.read())
    file_part['Content-Disposition'] = 'attachment; filename="file.txt"' 
    msg.attach(file_part)

email_string = msg.as_string()
print(email_string)

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, email_string)
s.quit()