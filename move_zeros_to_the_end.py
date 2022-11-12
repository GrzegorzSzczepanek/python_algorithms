def move_zeros(lst):
    newList = list(filter(lambda x: x!=0, lst))
    
    zeros = list(map(lambda x: int(x), list("0" * (len(lst) - len(newList)))))
    
    return newList + zeros
