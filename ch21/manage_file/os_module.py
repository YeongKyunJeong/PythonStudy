# os_module.py

import os

# (1) 현재 작업 디렉터리 확인 및 변경
# 현재 작업 디렉터리 확인
print(os.getcwd())
# 작업 디렉터리 변경
os.chdir(r"ch21\manage_file") 
print(os.getcwd())

# (2) 디렉터리 및 파일 목록 조회
print(f"디렉터리 파일 목록 : {os.listdir(".")}")

# (3) 디렉터리 생성 및 삭제
# 디렉터리 생성 : 이미 있으면 예외 발생
os.mkdir("test_dir")
# 디렉터리 삭제
os.rmdir("test_dir")

# (4) 파일 존재 여부 확인
# print(os.path.exists("file.txt"))
if os.path.exists(r"file.txt"):
    print("파일이 존재합니다.")

# (5) 파일 및 디렉터리 경로 다루기
folder = os.getcwd()
# 경로 합치기
print(os.path.join(folder, "file.txt"))

# 파일명만 추출
print(os.path.basename(f"{folder}/file.txt"))
# 디렉터리 경로 추출
print(os.path.dirname(f"{folder}/file.txt"))