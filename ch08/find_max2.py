# find_max2.py

su = [5, 4, 7, 10, 6]

def fmax(su):

    max_value = su[0]
    
    for num in su:
        if max_value < num:
            max_value = num
    
    return max_value

def fmin(su):

    min_value = su[0]
    
    for num in su:
        if min_value > num:
            min_value = num
    
    return min_value

print(fmax(su))
print(fmin(su))