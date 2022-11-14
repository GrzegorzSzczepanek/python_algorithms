def rgb(r, g, b):

    x = str(hex(r))[2:].upper()
    y = str(hex(g))[2:].upper()
    z = str(hex(b))[2:].upper()
    
    if r <= 16: x = "0" + x
    if g <= 16: y = "0" + y
    if b <= 16: z = "0" + z
    
    if r < 0: x = "00"
    if g < 0: y = "00"
    if b < 0: z = "00"
    
    if r > 255: x = "FF"
    if g > 255: y = "FF"
    if b > 255: z = "FF"
    
    return x + y + z
