from slack_sdk import WebClient  
from slack_sdk.errors import SlackApiError  

SLACK_API_TOKEN = "---"
SLACK_CHANNEL = "#python-slack-test"

client = WebClient(token=SLACK_API_TOKEN)

client.chat_postMessage(channel=SLACK_CHANNEL, text="Hello, Slack Message Test")