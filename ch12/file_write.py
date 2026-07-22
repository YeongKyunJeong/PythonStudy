# file_write.py

# 파일 열기
f = open(r"ch12\file2.txt", "w", encoding = 'utf-8')
# f = open(r"ch12\file1.txt", "w")

# 파일에 데이터 쓰기
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" %i
    # f.write(data)
    f.write(data)

# 파일 닫기
f.close()