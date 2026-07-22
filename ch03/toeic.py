# toeic.py

tscore = 920
tscore = 700
tscore = 550
tscore = 390


if tscore > 990 or tscore < 0:
    print("잘못된 점수입니다.")
elif tscore >= 900:
    print("당신의 점수는", tscore ,"점으로, 상위권입니다.")
elif tscore >= 600: 
# elif 600 < tscore <= 900:
# elif tscore <= 900 and tscore > 600:
    print("당신의 점수는", tscore ,"점으로, 중상위권입니다.")
elif tscore < 500 and tscore >= 400:
    print("당신의 점수는", tscore ,"점으로, 중위권입니다.")
elif tscore < 400:
    print("당신의 점수는", tscore ,"점으로, 하위권입니다.")