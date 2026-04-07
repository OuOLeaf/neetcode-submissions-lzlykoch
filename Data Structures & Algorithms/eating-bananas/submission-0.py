import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def pileHour(speed):
            count = 0
            for i in piles:
                hr = math.ceil(i / speed)
                count += hr
            return count
        r = sorted(piles)[-1]
        l = 1
        ans = -1
        while(l <= r):
            mid = (l + r) // 2
            hr = pileHour(mid)
            if hr <= h:
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        return ans