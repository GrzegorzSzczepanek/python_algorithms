def count_smileys(arr):
    eyes = [":", ";"]
    nose = ["-", "~"]
    smile = [")", "D"]
    
    smileys = 0
    
    for face in arr:
        if len(face) == 2:
            if face[0] in eyes and face[1] in smile:
                smileys += 1
        elif len(face) == 3:
            if face[0] in eyes and face[1] in nose and face[2] in smile:
                smileys += 1
                
    return smileys
