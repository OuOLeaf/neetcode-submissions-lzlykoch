class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while(l <= r):
            mid = (l + r) // 2
            me = nums[mid]
            le = nums[l]
            re = nums[r]
            # print(l, r, me)
            if me == target:
                return mid
            if le <= me:
                if le <= target and target <= me:
                    r = mid
                else:
                    l = mid + 1
            elif me <= re:
                if me <= target and target <= re:
                    l = mid
                else:
                    r = mid - 1
        return -1