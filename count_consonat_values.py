import re
def solve(s):
    a = list("abcdefghijklmnopqrstuvwxyz")
    s2 =  re.split('[aeiou]+', s)
    
    result = 0
    check = 0
    for element in s2:
        if check >= result:
            result = check
        check = 0
        for char in element:
            if char in a:
                check += a.index(char) + 1
            else:
                pass
        
            
            
    return result
