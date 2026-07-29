# stack_class.py
# 스택 구현 : 클래스 활용

class Stack:
    # 1. 스택 리스트
    def __init__(self):
        self.stack = [ ]

    # 2. push
    # 기능 : 스택에 데이터 추가
    # 입력 : 추가할 데이터
    # 출력 : None
    def push(self, item):
        self.stack.append(item)

    # 3. pop
    # 기능 : 스택에 데이터 제거
    # 입력 : 없음
    # 출력 : 스택의 Top 데이터
    def pop(self):
        # 스택이 비어있는 경우 고려
        if self.is_empty():
            return
        else:
            return self.stack.pop()

    # 4. 스택 내 데이터 유무 확인
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    # 5. 스택 Top 데이터 확인
    def peak(self):
        if self.is_empty():
            return
        else:
            return self.stack[-1]

    # 6. 스택 상태 반환
    def status_stack(self):
        return self.stack

if __name__ == "__main__":
    s1 = Stack()
    print(s1.peak())
    s1.pop()
    print(s1.status_stack())
    s1.push(1)
    s1.push(2)
    s1.pop()
    print(s1.status_stack())
    s1.push(3)
    s1.push(4)
    print(s1.peak())
    print(s1.status_stack())