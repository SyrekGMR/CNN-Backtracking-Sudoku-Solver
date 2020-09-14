import math

# Solver Backtracking Code

# Check if any subgrids are empty in need of filling.
# Update track parameter to the next empty subgrid.

def check_empty(arr, track):
    for i in range(9):
        for j in range(9):
            if arr[i, j] == 0:
                track[0] = i
                track[1] = j
                return True
    return False

# Check along row for validity of number

def check_row(row, num, arr):
    for i in range(9):
        if num == arr[row, i]:
            return False
    return True

# Check along column for validity of column

def check_col(col, num, arr):
    for i in range(9):
        if num == arr[i, col]:
            return False
    return True

# Locate 3x3 square of current subgrid

def locate_sq(col, row):
    col = math.floor(col/3)
    row = math.floor(row/3)
    
    return col, row

# Check validity of number inside its 3x3 square

def check_sq(col, row, num, arr):
    c, r = locate_sq(col, row)
    c = c * 3
    r = r * 3
    for i in range(r, r+3):
        for j in range(c, c+3):
            if num == arr[i, j]:
                return False
    return True

# Check overall validity of number at current location

def check_valid(row, col, num, arr):
    return check_row(row, num, arr) and check_col(col, num, arr) and check_sq(col, row, num, arr)


# Backtracking algorithm utilising the above functions

def solver(arr):
    track = [0, 0]   
    
    if not check_empty(arr, track):
        return True
    
    for num in range(1, 10):
        if check_valid(track[0], track[1], num, arr):
            
            arr[track[0], track[1]] = num
            
            if solver(arr):
                return True
                        
            arr[track[0], track[1]] = 0     
        
    return False

def backtracking(arr):
    if(solver(arr)):
        print(arr)
    else:
        print("NO SOLUTIONS!")