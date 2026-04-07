class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        ans = -1
        while(l <= r):
            mid = (l + r) // 2
            num = nums[mid]
            if num == target:
                return mid
            elif num < target:
                l = mid + 1
            elif num > target:
                r = mid - 1
        return ans