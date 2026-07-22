# dup_if.py

# 다양한 if문의 형태
# 기본 if문
# if 조건식:
#     코드블록

# if 조건식:
#     코드블록
# else:
#     코드블록
    
# if 조건식1:
#     코드블록
# elif 조건식2:
#     코드블록
# else:
#     코드블록

# 중첩된 if문
# if 조건식1:
#     코드블록1
#     if 조건식2:
#         코드블록2
# else:
#     코드블록3
#     if 조건식3:
#         코드블록4
#     else:
#         코드블록

# 여러번 중첩된 if문
# if 조건식1:
#     코드블록1
#     if 조건식2:
#         코드블록2
#         if 조건식3:
#             코드블록3

text = "토익 점수를 입력해주세요."
tscore = int(input(text))
# tscore = 700
# tscore = 550
# tscore = 390


if tscore > 990 or tscore < 0:
    print("잘못된 점수입니다.\n")
elif tscore >= 900:
    if tscore >= 950:
        print("최", end = "")
    else:
        print("차", end = "")
    print("상위권")
elif tscore >= 600: 
    print("중상위권")
elif tscore < 500 and tscore >= 400:
    print("중위권")
elif tscore < 400:
    print("하위권")