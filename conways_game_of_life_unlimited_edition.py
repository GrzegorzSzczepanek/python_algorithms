def get_generation(cells, generations):
    alive = []
    dead = []
    alive_coords = []
    dead_coords = []
    arr = cells
    if generations == 0:
        return arr
    for i0 in range(0, generations):
        for i1 in range(0, len(arr)):
            for i2 in range(0, len(arr)):
                count1 = 0
                # check if there is alive cell in horizontal and vertical axis
                if i2 - 1 >= 0 and arr[i1][i2 - 1] == 1:
                    count1 += 1
                if i1 - 1 >= 0 and arr[i1 - 1][i2] == 1:
                    count1 += 1
                if i1 + 1 < len(arr) and arr[i1 + 1][i2] == 1:
                    count1 += 1
                if i2 + 1 < len(arr) and arr[i1][i2 + 1] == 1:
                    count1 += 1

                # check if there is alive cell in diagonals

                if i2 - 1 >= 0 and i1 - 1 >= 0 and arr[i1 - 1][i2 - 1] == 1:
                    count1 += 1
                if i2 + 1 < len(arr) and i1 + 1 < len(arr) and arr[i1 + 1][i2 + 1] == 1:
                    count1 += 1
                if i2 - 1 >= 0 and i1 + 1 < len(arr) and arr[i1 + 1][i2 - 1] == 1:
                    count1 += 1
                if i2 + 1 < len(arr) and i1 - 1 >= 0 and arr[i1 - 1][i2 + 1] == 1:
                    count1 += 1

                if (count1 == 2 or count1 == 3) and arr[i1][i2] == 1:
                    alive_coords.append([i1, i2])
                elif count1 == 3 and arr[i1][i2] == 0:
                    alive_coords.append([i1, i2])
                else:
                    dead_coords.append([i1,i2])
        for i in alive_coords:
            arr[i[0]][i[1]] = 1
        for i in dead_coords:
            arr[i[0]][i[1]] = 0
                
    return arr
