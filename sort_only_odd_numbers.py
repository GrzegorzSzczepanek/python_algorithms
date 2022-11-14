def sort_array(source_array):
    odds = sorted(list(filter(lambda x: x%2!=0, source_array)))
    oddIndex = 0
    res = []
    for i in source_array:
        if i % 2 == 0:
            res.append(i)    
        elif i % 2 != 0:
            res.append(odds[oddIndex])
            oddIndex += 1
    
    return res
