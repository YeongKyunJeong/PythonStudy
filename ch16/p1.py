# p1.py
# 문제 1: 괄호 짝 검사
# 기능 : 문자열에 포함된 짝이 올바르게 사용되었는지 확인
#        스택 활용
# 입력 : 문자열
# 반환 : True : 짝이 맞음, False : 짝 안 맞음

leftset = {"(", "{", "["}
rightset = {")", "}", "]"}

# inputstr = input()
from stack_class import Stack

def solveex(inputstr):
    stack = []

    for char in inputstr:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            top = stack.pop()
            if char == ")" and top != "(":
                return False
            elif char == "}" and top != "{":
                return False
            elif char == "]" and top != "[":
                return False
    if stack:
        return False 

    return True


def solve(inputstr):
    stack = Stack()
    for s in inputstr:
        if s in leftset:
            stack.push(s)
        elif s in rightset:
            # if stack.is_empty:
            #     return False
            # elif s == ")" and stack.peak() == "(":
            if s == ")" and stack.pop() == "(":
                continue
            elif s == "}" and stack.pop() == "{":
                continue
            elif s == "]" and stack.pop() == "[":
                continue
            else:
                return False
        else:
            continue

    if stack.is_empty():
        return True
    return False

text1 = "(a+b)"
text2 = "(a+b]}"
text3 = "[{(x+y)+3}-4]"
text4 = "[{x+y}+3)-4]"
print(solveex(text1))
print(solveex(text2))
print(solveex(text3))
print(solveex(text4))
print(solve(text1))
print(solve(text2))
print(solve(text3))
print(solve(text4))