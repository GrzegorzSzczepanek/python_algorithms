def validate(rows, columns):
    inRow = []
    inColumns = []
    square = [] 
    for i in rows:
        for el in i:
            if el in inRow or el == 0:
                return False
            else:
                inRow.append(el)
        inRow = []
    
    for i in columns:
        for el in i:
            if el in inColumns:
                return False
            else:
                inColumns.append(el) 
        inColumns = []
    
    for i in range(0,3):
        for el in range(0,3):
            square.append(rows[i][el])
    if len(square) != len(set(square)):
        return False

    square = []
    
    for i in range(3,6):
        for el in range(3,6):
            square.append(rows[i][el])
    if len(square) != len(set(square)):
        return False
    square = []    
    for i in range(6,9):
        for el in range(6,9):
            square.append(rows[i][el])
    
    if len(square) != len(set(square)):
        return False
    square = []
    
    return True

def valid_solution(board):
    rows = []
    columns = [[],[],[],[],[],[],[],[],[]]
    for i in board:
        rows.append(i)
        for el in range(0,len(i)):
            columns[el].append(i[el])
            
    return validate(rows, columns)

            
            
        
