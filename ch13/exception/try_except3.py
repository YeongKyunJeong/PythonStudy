# try_except3.py

# path = ""
# f = open(path)      # FileNotFoundError
# s = f.readline()
# s.strip()           # 문자열 앞뒤 공백, 줄바꿈, 이스케이프 코드를 제거함
# i = int(s.strip())

path = r"ch13\exception\myfile.txt"
try:
    # f = open(path, "w")
    # f.write("hello")
    # f.close()
    f = open(path)               # FileNotFoundError
    s = f.readline()   
    i = int(s.strip())           # 문자열 앞뒤 공백, 줄바꿈, 이스케이프 코드를 제거함
except (RuntimeError, TypeError, NameError):
    print("RuntimeError, TypeError, or NameError occurs")

except FileNotFoundError as e:
    print("파일 찾기 실패")
except ValueError as e:
    print("정수형으로 변환할 수 없습니다")
    print(e)
except Exception as e:
    print("예측되지 않은 에러 발생")
    print(e)
    
