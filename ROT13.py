def rot13(message):
    a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    res = ""
    for char in message:
        if char in b:
            res += b[a.index(char)]
        else:
            res += char
    
    return res
