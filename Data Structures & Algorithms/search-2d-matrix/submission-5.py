class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def isNear(ls, target):
            left = 0
            right = len(ls) - 1
            pos = -1
            while(left <= right):
                mid = (left + right) // 2
                # print(left, right, ls[mid])
                if target == ls[mid]:
                    return mid
                elif target > ls[mid]:
                    left = mid + 1
                    pos = mid
                elif target < ls[mid]:
                    right = mid - 1
            return pos
        
        def isThere(ls, target):
            left = 0 
            right = len(ls) - 1
            while(left <= right):
                mid = (left + right) // 2
                if ls[mid] == target:
                    return True
                elif ls[mid] > target:
                    right = mid - 1
                elif ls[mid] < target:
                    left = mid + 1
            return False   
        
        lf = [k[0] for k in matrix]
        pos = isNear(lf, target)
        # print(pos)
        ans = isThere(matrix[pos], target) 

        return ans