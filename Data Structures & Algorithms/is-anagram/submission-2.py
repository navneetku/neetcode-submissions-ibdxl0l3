class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# Time Complexity: O(n)
# Space Complexity: O(n)
        