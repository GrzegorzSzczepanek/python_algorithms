def solution(s):
    if len(s) % 2 != 0:
        s += "_"
    
    res = []
    char = 0
    for i in range(0, len(s) - 1):
        if char >= len(s) - 1:
            return res
        
        res.append(s[char] + s[char+1])
        char += 2

    return res

# def solution(s):
#     if len(s) % 2 != 0:
#         s += "_"
#     res = []
#     for i in range(0, len(s) - 1, 2):
#         res.append(s[i:i+2:])
        
#     return res
