# optimize.py

from scipy.optimize import minimize
# 단순 2차 함수 최적화

def f(x):
    return x**2 + 4*x + 4

result = minimize(f, x0 = 0)
print(f"Optimal Value : {result.x}")