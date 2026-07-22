# select_sorting1.py

ca = [21, 10, 11, 15, 13]

def fselsort(cb):
    
    for i in range(len(cb)):
        idx_min = i
        min_val = cb[i]
        for j in range(i + 1, len(cb)):
            if min_val > cb[j]:
                min_val = cb[j]
                idx_min = j
            
        cb[idx_min], cb[i] = cb[i], cb[idx_min]

    return

fselsort(ca)
print(ca)
            
