import schedule
import time

def job():
    print("Test입니다.")

# 3초마다 job 실행
schedule.every(3).seconds.do(job)

# 예약 작업 실행하기

while True:
    schedule.run_pending()  # 예약된 작업을 확인하고 실행
    time.sleep(1)          # 1초 대기하여 CPU 사용량 감소