from slack_sdk import WebClient
import os, time
import datetime

# Slack API 토큰과 메시지를 보낼 채널 설정
SLACK_API_TOKEN = "----"
SLACK_CHANNEL = "C07LS9ZN8MS"  # channel id 를 써야 함
DIR_PATH = 'static'

def send_slack_message(message):
    client = WebClient(token=SLACK_API_TOKEN)
    client.chat_postMessage(channel=SLACK_CHANNEL, text=message)

pre_file = set(os.listdir(DIR_PATH))

while True:
    current_file = set(os.listdir(DIR_PATH))
    result_files = current_file - pre_file
    
    for result_file in result_files:
        if result_file.endswith(".php"):
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            send_slack_message(f"Message sent successfully: Warning: A new .php file was uploaded to the directory!\nFile: {result_file}\nTime:{current_time}")

    pre_file = current_file
    time.sleep(1)







def upload_file(channel, file_path, message):
    # WebClient 인스턴스 생성
    client = WebClient(token=SLACK_API_TOKEN)
    
    response = client.files_upload_v2(
        channel=channel, 
        file=file_path,
        initial_comment=message
    )

# 파일 업로드 및 메시지 전송 함수 호출
upload_file(SLACK_CHANNEL, r"C:\python_ex\example.txt", "Here is the file you requested!")