class Solution:
    def spiralOrder(self, matrix):
        '''Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

'''
        res = []
        while matrix:
            res.extend(matrix.pop(0)) # left to right
            print(res)
            if matrix and matrix[0]: # top to dwon
                for row in matrix:
                    res.append(row.pop())
            print(res)
            if matrix: # right to left
                res.extend(matrix.pop()[::-1])
            if matrix and matrix[0]: # bottom to up
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res