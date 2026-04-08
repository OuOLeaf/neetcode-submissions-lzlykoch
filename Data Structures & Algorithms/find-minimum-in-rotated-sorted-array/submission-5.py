class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        ans = 1001
        while(l <= r):
            fe = nums[l]
            le = nums[r]
            mid = (l + r) // 2
            me = nums[mid]
            print(l, r, nums[mid])
            if ans > nums[mid]:
                ans = nums[mid]
            if ans > fe:
                ans = fe
            if le > me:
                r = mid - 1
            elif fe <= me:
                l = mid + 1
            
        return ans