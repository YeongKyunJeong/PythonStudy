# week.py

text = "영어로 번역하고 싶은 요일을 입력하세요.\n"
date = input(text)
if date == "월요일":
    print("Monday")
elif date == "화요일":
    print("Tuesday")
elif date == "수요일":
    print("Wednesday")
elif date == "목요일":
    print("Tursday")
elif date == "금요일":
    print("Friday")
elif date == "토요일":
    print("Saturday")
elif date == "일요일":
    print("Sunday")
else :
    print("요일이 잘못 입력됐습니다.")