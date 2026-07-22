# type_hint.py

def add(arg1: int, arg2: int) -> int:
    return arg1 + arg2

print((add(3, 5)), end=" ")
print(type(add(3, 5)))
print((add(3.5, 5)), end=" ")
print(type(add(3.5, 5)))