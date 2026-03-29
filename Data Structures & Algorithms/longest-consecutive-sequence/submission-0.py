class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in numSet:
                length = 0
                while num + length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

# Time Complexity: O(n) (Since we will reach each element a max of twice so it won't be n^2.)
# Space Complexity: O(n)