# recursive.py

# 재귀함수
# def 함수명(매개변수):
#     코드블록
#     함수명(인수)
#     return 반환값

# 함수명(인수)

def count_donw(n):
    if n == 0:
        print("완료!")
        return
        
    print(n)
    count_donw(n-1)

count_donw(5)