import smtplib
from email.mime.text import MIMEText

send_email = "fkelfkenl10@naver.com"
send_pwd = "Lch885233@"
recv_email = "chaehyun.forest@gmail.com"

smtp_name = "smtp.naver.com" 
smtp_port = 587              

text = """
메일 내용 입력
텍스트1
텍스트2
"""

msg = MIMEText(text, 'plain', 'utf-8') 
             

email_string = msg.as_string()
print(email_string)

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, email_string)
s.quit()