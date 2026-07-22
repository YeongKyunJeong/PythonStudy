# turtle_ex1.py

# import turtle

# turtle.shape('turtle')

# for x in range(1, 100, 1):
#     turtle.forward(x)       # x걸음만큼 전진
#     turtle.left(90)         # 90도만큼 왼쪽으로 회전

from turtle import *
from turtle import shape
from turtle import forward
from turtle import left

shape('turtle')

for x in range(1, 100, 1):
    forward(x)       # x걸음만큼 전진
    left(90)         # 90도만큼 왼쪽으로 회전
