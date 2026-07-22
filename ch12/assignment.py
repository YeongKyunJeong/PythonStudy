# assignment.py
# with open("test.txt", "w") as file:
#     file.write("Hello, World!")
# print(file.closed)

# pizzas = ["페퍼로니피자 3000", "치즈피자 3200", "콤비네이션피자 3500"]

# with open("./pizza_file1.txt", "w", encoding = "utf-8") as f:
#     f.write("\n".join(pizzas))

# pizzas_new = ["불고기피자 3600", "해산물피자 3800"]

# with open("./pizza_file1.txt", "a", encoding = "utf-8") as f:
#     f.write("\n" + "\n".join(pizzas_new))

# with open("./pizza_file1.txt", "r", encoding = "utf-8") as f:
#     print(f.read())

pizza_list = []
with open("./pizza_file1.txt", "r", encoding = "utf-8") as f:
    pizza_data = f.readlines()
    for pizza in pizza_data:
        pizza_list.append(pizza.split(" ")[0])
print(pizza_list)

