def count(string):
    res = {}
    
    for char in string:
        if not char in res.keys():
            res.update({char : string.count(char)})
            
    return res
