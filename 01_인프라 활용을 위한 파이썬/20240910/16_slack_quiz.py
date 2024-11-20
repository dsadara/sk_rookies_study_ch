import os, time
import datetime
from slack_sdk import WebClient  
from slack_sdk.errors import SlackApiError  

DIR_PATH = 'static'
SLACK_API_TOKEN = "----"
SLACK_CHANNEL = "C07LS9ZN8MS"  # channel id 를 써야 함

pre_file = set(os.listdir(DIR_PATH))

while True:
    current_file = set(os.listdir(DIR_PATH))
    result_files = current_file - pre_file
    
    for result_file in result_files:
        print(f"새로운 탐지 파일: {result_file}")
        file_path = os.path.join(os.getcwd(), DIR_PATH, result_file)
        # print(file_path)
        if result_file.endswith(".php"):
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"File: {result_file}")
            print(f"Time: {current_time}")
            client = WebClient(token=SLACK_API_TOKEN)
            client.chat_postMessage(channel=SLACK_CHANNEL, text="Hello, Slack Message Test")

    pre_file = current_file
    time.sleep(1)