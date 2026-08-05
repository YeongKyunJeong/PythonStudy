# shutil_module.py

import shutil
import os

# (1) 파일 복사
# shutil.copy("source.txt", "destination.txt")
# # 메타 데이터를 유지하며 복사
# shutil.copy2("source.txt", "destination.txt")

path = r"ch21\manage_file"
src = f"{path}/file.txt"
dst = f"{path}/copiedfile.txt"
shutil.copy(src, dst)
# 메타 데이터를 유지하며 복사
# shutil.copy2(src, dst)

# (2) 디렉터리 복사
# shutil.copytree(src, dst)

# 디렉터리 생성
folder = f"{path}/test_dir"
if not os.path.exists(folder):
    os.mkdir(folder)

# 파일 복사
src = f"{path}/file.txt"
dst = f"{path}/test_dir/file.txt"
if not os.path.exists(dst):      # 파일이 존재하지 않으면
    shutil.copy(src, dst)        # 복사

# 디렉터리 전체 복사
src = f"{path}/test_dir"
dst = f"{path}/copied_test_dir"
if not os.path.exists(dst):
    shutil.copytree(src, dst)

# (3) 파일 및 디렉터리 이동
src = f"{path}/copiedfile.txt"
dst = f"{path}/copied_test_dir/copiedfile.txt"
if not os.path.exists(dst):
    shutil.move(src, dst)

# (4) 파일 및 디렉터리 삭제
# 디렉터리 및 하위 파일 모두 삭제
dir1 = f"{path}/test_dir"
dir2 = f"{path}/copied_test_dir"
shutil.rmtree(dir1)
shutil.rmtree(dir2)