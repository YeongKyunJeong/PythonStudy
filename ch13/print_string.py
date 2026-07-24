# print_string.py

### 다양한 문자열 사용(출력) 방법
# 표준 출력 함수 : print(인수)
# 1. 기능 : 인수를 모니터에 출력
# 2. 인수 : object 클래스 객체 = 모든 자료형
# 3. 반환 : 없음(None)

# 기본 형식
name = "홍길동"
age = 510
print("이름:", name, "나이", age)

# 1. % d연산자 사용 방식
# 서식문자 활용
# %s : 문자열
# %d : 10진수
# %f : 실수형
# %x : 16진수
print("이름: %s 나이 %d"%(name, age))

# 2. format() 메서드
print("이름: {} 나이 {}".format(name, age))

# 3. f-string
print(f"이름: {name} 나이 {age}")


