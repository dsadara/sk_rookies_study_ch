from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Slack API 토큰과 메시지를 보낼 채널 설정
SLACK_API_TOKEN = "----"
SLACK_CHANNEL = "C07LS9ZN8MS"  # channel id 를 써야 함

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