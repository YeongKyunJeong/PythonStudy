# find_root.py

from scipy.optimize import root

def equation(x):
    return x**2 - 4

# sol = root(equation, x0 = 1)
# print(f"Root : {sol.x}")

# sol = root(equation, x0 = -1)
# print(f"Root : {sol.x}")

roots = []
for x0 in [-10, -1, 1, 10]:
    sol = root(equation, x0 = [x0])
    print(f"Root : {sol.x}")
    if sol.success:
        roots.append(sol.x[0])
print(roots)

roots = []
for x0 in [-10, -1, 1, 10]:
    sol = root(equation, x0 = x0)
    print(f"Root : {sol.x}")
    print(type(sol.x))
    if sol.success:
        roots.append(sol.x)
print(roots)