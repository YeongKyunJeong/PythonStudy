# generator2_1.py

# 2. 제너레이터 컴프리헨션 사용 예제
import time
def longtime_job():
    print("job start")
    time.sleep(1)      # 1초간 프로그램 지연
    return "done"

gen_job = (longtime_job() for item in range(5))
print(gen_job)
for i in gen_job:
    # print(i)
    continue

# print(gen_job)