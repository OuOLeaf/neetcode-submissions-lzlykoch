class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) * len(matrix[0]) - 1
        ncol = len(matrix[0])
        while(l <= r):
            m = (l + r) // 2
            col = m % ncol
            row = m // ncol
            print(l, r, m, matrix[row][col])
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = m + 1
            elif matrix[row][col] > target:
                r = m - 1
        return False