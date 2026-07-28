# generator1.py

def simple_generator():
    print("실행")
    yield 'a'
    yield 'b'
    yield 'c'

g = simple_generator()
# print(type(g))
# print(g)

print(next(g))
print(next(g))
for i in iter(g):
    print(i)
print(hasattr(g, "__next__"))
print("__next__" in dir(g))
print(simple_generator.__dict__)

def generator_example():
    for i in range(1, 10):
        yield i*i

g = generator_example()
for i in g:
    print(i)
# print(g.__next__())
print(hasattr(g, "__init__"))
print("__next__" in dir(g))
# print(dir(g))

gen = (i*i for i in range(1, 10))
for i in gen:
    print(i)