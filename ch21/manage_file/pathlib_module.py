# pathlib_module.py
# path = r"ch21\classify_fire"

from pathlib import Path

# 1. pathlib 기본 기능 : 디렉터리 확인
# 현재 작업 디렉터리 확인
print(Path.cwd())
# 홈 디렉터리(사용자 디렉터리) 확인
print(Path.home())

# 2. 경로 객체 생성 및 조작
folder = r"ch21\classify_file"
path = Path(folder)
# pathlib의 경로 결합 연산자 '/'로 경로 결합
print(path / "file.txt")

# 3. 디렉터리 및 파일 존재 여부 확인
file = r"ch21\manage_file\file.txt"
path = Path(file)
# 존재 여부 확인
print(path.exists())
# 파일 여부 확인
print(path.is_file())
# 경로 여부 확인
print(path.is_dir())

# 존재하지만 일반적인 파일이 아닌 경우
# - 디렉터리 : is_dir()로 확인
# - 심볼릭(바로가기) 링크 : is_symlink()로 확인
# - 장치 파일 (리눅스/맥 시스템의 /dev/ 파일 등)
# - 소켓 파일 (네트워크 통신용) 

# pathlib을 활용한 파일 및 디렉터리 조작
# 1. 디렉터리 생성 및 삭제
new_folder = r"ch21\classify_file\new_folder"
path = Path(new_folder)
path.mkdir(exist_ok= True) # exist_ok : 이미 존재하면 덮어쓰기
 # 폴더 삭제
path.rmdir()

# 2. 파일 생성 및 삭제
file = r"ch21\classify_file\file.txt"
file_path = Path(file)
file_path.touch() # 빈 파일(용량이 0인 파일) 생성
file_path.touch(exist_ok = False) # 덮어쓰기 방지
file_path.unlink() # 파일 삭제