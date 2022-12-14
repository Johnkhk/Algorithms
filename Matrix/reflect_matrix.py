m = [[1,2,3],[4,5,6],[7,8,9]]

# main diag 0,0
# 1 2 3    1 4 7
# 4 5 6 -> 2 5 8 -> 0,1 -> 1,0
# 7 8 9    3 6 9

def reflect(m):
    # should be a square
    rows,cols = len(m),len(m[0])
    for r in range(rows):
        for c in range(r+1,cols):
            m[r][c],m[c][r] = m[c][r],m[r][c]
# off diag
# 1 2 3    9 6 3
# 4 5 6 -> 8 5 2 -> 0,0 -> 2,2, 0,1-> 1,2
# 7 8 9    7 4 1

def reflect2(m):
    # should be a square
    rows,cols = len(m),len(m[0])
    for r in range(rows):
        for c in range(cols-1-r):
            m[r][c],m[cols-1-c][rows-1-r] = m[cols-1-c][rows-1-r],m[r][c]

    return m

m = reflect2(m)
for r in m:
    print(r)  
