# func_return.py

# def fplusminus(arg):
#     if arg > 0:
#         return "plus"
#     elif arg < 0:
#         return "minus"
    
# stra = fplusminus(0)
# print(stra, type(stra))

def fplusminus(arg):
    if arg > 0:
        return "plus"
    elif arg < 0:
        return "minus"
    else:
        return "zero"
    
stra = fplusminus(0)
print(stra, type(stra))