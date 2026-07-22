# default2.py

def persona(width, height):
    print("width =", width, end = ", ")
    print("height =", height)
    
# def persona():
#     print("without parameter")
    
def personb(width = 4, height = 3):
    print("width =", width, end = ", ")
    print("height =", height)
persona(10, 20)
# persona()
personb()