def find_nb(m):
    n = 0
    v = 0
    
    while v < m:
        v += (n + 1) ** 3
        n += 1
    
    return -1 if v != m else n
