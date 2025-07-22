def searchMatrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    # step1 - we find the correct row
    t_row = -1
    top, bottom = 0, len(matrix)-1
    while top <= bottom:
        m_row = (top+bottom)//2
        if matrix[m_row][0] > target:
            bottom = m_row - 1
        elif matrix[m_row][-1] < target:
            top = m_row + 1
        else:
            t_row = m_row
            break
    
    if t_row == -1:
        return False # target not within bounds of any row.
    # step2 - search for the target in this discovered row
    l, r = 0, cols-1
    while l <= r:
        m = (l+r)//2
        if matrix[t_row][m] == target:
            return True
        elif matrix[t_row][m] < target:
            l = m+1
        else:
            r = m-1
    return False
    
        

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
res = searchMatrix(matrix, target)
print(res)