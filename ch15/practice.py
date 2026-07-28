# practice.py

# food = ["김밥", "만두", "양념치킨", "족발", "피자", "쫄면", "라면"]
# iter_food = food.__iter__()
# for i in range(len(food)):
#     print(iter_food.__next__())

# print( "__next__" in dir(iter_food))
# print(hasattr(iter_food, "__iter__"))

# class My_iterator:
#     def __init__(self, data):
#         self.data = data
#         self.position = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.position > len(self.data):
#             raise StopIteration
#         result = self.data[self.position]
#         self.position += 1
#         return result

# iter_food2 = My_iterator(food)
# for i in range(len(food)):
#     print(iter_food2.__next__())

# iter_food3 = (item for item in food)

# for i in range(len(food)):
#     print(iter_food3.__next__())

# def write_file(file_path: str):
#     with open(file_path, "w") as file:
#         file.write(data)

# def read_file(file_path: str):
#     with open(file_path, 'r') as file:
#         for line in file.readlines():
#             yield line.strip()

# path = r"ch15\file.txt"
# data = """The mission of the Python Software Foundation is to promote, 
# protect, and advance the Python programming language, 
# and to support and facilitate the growth of a diverse 
# and international community of Python programmers."""
# write_file(path)
# lines = read_file(path)

# print(lines.__next__())



# subjects = ['수학', '과학', '영어']
# scores = [80, 60, 70]
# scores = {subject : score for subject, score in zip(subjects, scores)}
# grade = {sub : "합격" if sco >= 80 else "불합격" 
#          for sub, sco in scores.items() }
# print(grade)

def write_file(path:str, data:str):
    with open(path, 'w', encoding = "utf-8") as file:
        file.write(data)

def read_file(path:str):
    with open(path, 'r', encoding = 'utf-8') as file:
        for line in file.readlines():
            yield line.strip()


path = r"ch15\file.txt"
data = """The mission of the Python Software Foundation is to promote, 
protect, and advance the Python programming language, 
and to support and facilitate the growth of a diverse 
and international community of Python programmers."""

write_file(path, data)
g = read_file(path)
print(g.__next__())
print(g.__next__())
print(g.__next__())