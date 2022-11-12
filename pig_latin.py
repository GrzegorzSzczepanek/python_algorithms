import re
def pig_it(text):
    arr = []
    
    for i in text.split(" "):
        if re.search("[a-zA-Z]", i):
            char = i[0]
            arr.append(i[1:] + char + "ay")
        else:
            arr.append(i)
            
    return " ".join(arr)
