class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        ans = nums[0]
        while(l <= r):
            fe = nums[l]
            le = nums[r]
            mid = (l + r) // 2
            me = nums[mid]
            # print(l, r, me)
            if ans > me:
                ans = me
            if le > me:
                r = mid - 1
            elif le <= me:
                l = mid + 1
            
        return ans