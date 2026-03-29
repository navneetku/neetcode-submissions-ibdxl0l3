class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                return True
        return False

# Time Complexity: O(n)
# Space Complexity: O(n)
