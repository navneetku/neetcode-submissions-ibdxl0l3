class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# Time Complexity: O(nlogn)
# Space Complexity: O(1)
        