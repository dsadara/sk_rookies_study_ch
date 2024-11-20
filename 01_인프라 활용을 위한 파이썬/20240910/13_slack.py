# requests 라이브러리를 가져와 HTTP 요청을 보낼 수 있도록 함
import requests  

# Slack에서 제공된 Webhook URL을 저장 (실제 URL로 대체 필요)
slack_url = "https://hooks.slack.com/services/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"  

# 슬랙으로 메시지를 전송하는 함수
def sendSlackWebHook(strText):
    headers2 = {
		    # 요청 헤더에 JSON 형식의 데이터를 전송할 것임을 명시
        "Content-type": "application/json"  
    }
    
    data = {
		    # 슬랙에 전송할 메시지 내용을 포함하는 JSON 데이터 생성
        "text": strText  
    }
    # requests.post()를 사용하여 Slack Webhook URL로 POST 요청을 보냄
    # headers와 json 파라미터를 사용하여 요청 데이터와 헤더를 전송
    res = requests.post(slack_url, headers=headers2, json=data)

    # 요청이 성공적으로 처리되었는지 확인 (status_code 200: 성공)
    if res.status_code == 200:
        return "OK"  # 성공적으로 메시지가 전송되었음을 알림
    else:
        return "Error"  # 에러가 발생한 경우 에러 메시지를 반환

# 함수 호출: "파이썬 자동화 슬랙 메시지 테스트" 메시지를 슬랙으로 전송
print(sendSlackWebHook("파이썬 자동화 슬랙 메시지 테스트"))
