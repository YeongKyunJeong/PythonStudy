# mex5.py

print("mex5.py")

class Cvalue:

    def __init__(self):
        self.lista = []

    def add(self, num):
        self.lista.append(num)

    def fprint(self):
        print(self.lista)

def plus(a, b):
    c = a + b
    return c

if __name__ == "__main__":
    p5 = Cvalue()
    p5.add(1)
    p5.add(2)
    p5.add(3)
    p5.fprint()
    print(plus(10, 20))
