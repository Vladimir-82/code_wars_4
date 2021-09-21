def trace(matrix):
    '''
    Matrix Trace
    '''
    return None if not matrix or len(matrix) != len(matrix[0]) else sum([matrix[i][i] for i in range(len(matrix))])



print(trace([[1, 2, 3], [4, 5, 6], [7, 8, 9], [5,4,23]]))