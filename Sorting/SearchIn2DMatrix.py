class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

        :param matrix:
        :param target:
        :return:
        '''
        m = len(matrix)
        if len(matrix) == 0:
            return False
        n = len(matrix[0])

        left = 0
        right = n * m - 1

        while left <= right:
            mid_idx = (left + right) // 2
            mid_ele = matrix[mid_idx // n][mid_idx % n]

            if target == mid_ele:
                return True
            else:
                if target < mid_ele:
                    right = mid_idx - 1
                else:
                    left = mid_idx + 1
        return False