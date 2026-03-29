class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l<=r:
            m = (l + r)//2
            rate = 0
            for i in range(len(piles)):
                rate += math.ceil(piles[i]/m)
            if rate <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res

# Time Complexity: O(log(max(piles))*len(piles))
# Space Complexity: O(1)