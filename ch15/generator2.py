# generator2.py

# 1. 리스트 컴프리헨션 사용 예제
import time
def longtime_job():
    print("job start")
    time.sleep(1)      # 1초간 프로그램 지연
    return "done"

list_job = [longtime_job() for item in range(5)]
print(list_job)
print(list_job[0])