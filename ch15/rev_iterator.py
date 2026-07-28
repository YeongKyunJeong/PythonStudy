# rev_iterator.py

class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.position = len(data) - 1

    def __iter__(self):
        return self.data

    def __next__(self):
        if self.position < 0:
            raise StopIteration
        result = self.data[self.position]
        self.position -= 1
        return result

ri = ReverseIterator([1, 2, 3, 4, 5])
print(next(ri))

print(type(ri))

print(hasattr(ri, "__next__"))
print("__iter__" in dir(ri))
