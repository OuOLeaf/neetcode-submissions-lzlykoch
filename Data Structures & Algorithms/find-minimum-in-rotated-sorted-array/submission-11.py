class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while(l <= r):
            fe = nums[l]
            le = nums[r]
            mid = (l + r) // 2
            me = nums[mid]
            # print(l, r, me)
            if le > me:
                r = mid 
            elif le <= me:
                l = mid + 1
            
        return me