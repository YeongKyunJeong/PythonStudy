# find_max1.py

ca = [10, 17, 13, 11]
max_value = ca[0]
# for i in range(1, len(ca)):
#     max_value = max(max_value, ca[i])

for num in ca:
    # max_value = max(max_value, num)
    if max_value < num:
        max_value = num

print(max_value)